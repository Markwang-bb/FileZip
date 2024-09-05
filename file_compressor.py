import sys
import os
import logging
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel, QSpinBox, QProgressBar, QCheckBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import zipfile

# 设置日志记录
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class CompressThread(QThread):
    update_progress = pyqtSignal(int)
    compression_done = pyqtSignal(str)
    compression_error = pyqtSignal(str)

    def __init__(self, input_file, target_size):
        super().__init__()
        self.input_file = input_file
        self.target_size = target_size
        self.is_cancelled = False

    def run(self):
        output_file = self.input_file + '.zip'
        try:
            logging.info(f"开始压缩文件: {self.input_file}")
            logging.info(f"目标大小: {self.target_size} 字节")

            original_size = os.path.getsize(self.input_file)
            compression_level = 9  # 从最高压缩级别开始

            while compression_level > 0 and not self.is_cancelled:
                with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zipf:
                    zipf.write(self.input_file, os.path.basename(self.input_file))

                current_size = os.path.getsize(output_file)
                logging.info(f"当前压缩级别: {compression_level}, 当前大小: {current_size} 字节")

                if current_size <= self.target_size:
                    break

                compression_level -= 1
                progress = int((9 - compression_level) / 9 * 100)
                self.update_progress.emit(progress)

            if self.is_cancelled:
                logging.info("压缩已取消")
                os.remove(output_file)
                self.compression_error.emit("压缩已取消")
            elif current_size > self.target_size:
                logging.warning(f"无法达到目标大小。最终大小: {current_size} 字节")
                self.compression_done.emit(output_file)
            else:
                logging.info(f"压缩成功。最终大小: {current_size} 字节")
                self.compression_done.emit(output_file)

        except Exception as e:
            logging.error(f"压缩过程中发生错误: {str(e)}")
            self.compression_error.emit(str(e))

    def cancel(self):
        self.is_cancelled = True

class FileCompressor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.select_button = QPushButton('选择文件')
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        self.file_label = QLabel('未选择文件')
        layout.addWidget(self.file_label)

        self.auto_size_checkbox = QCheckBox('自动设置目标大小为原文件的一半')
        self.auto_size_checkbox.stateChanged.connect(self.update_target_size)
        layout.addWidget(self.auto_size_checkbox)

        self.size_label = QLabel('目标大小 (MB):')
        layout.addWidget(self.size_label)

        self.size_input = QSpinBox()
        self.size_input.setRange(1, 10000)
        self.size_input.setValue(50)  # 默认设置为50MB
        layout.addWidget(self.size_input)

        self.compress_button = QPushButton('压缩')
        self.compress_button.clicked.connect(self.compress_file)
        layout.addWidget(self.compress_button)

        self.cancel_button = QPushButton('取消')
        self.cancel_button.clicked.connect(self.cancel_compression)
        self.cancel_button.setVisible(False)
        layout.addWidget(self.cancel_button)

        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)

        self.status_label = QLabel('')
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.setWindowTitle('文件压缩器')
        self.setGeometry(300, 300, 300, 250)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, '选择文件')
        if file_name:
            self.file_label.setText(file_name)
            logging.info(f"已选择文件: {file_name}")
            self.update_target_size()

    def update_target_size(self):
        if self.auto_size_checkbox.isChecked() and self.file_label.text() != '未选择文件':
            original_size = os.path.getsize(self.file_label.text())
            target_size = max(1, original_size // (2 * 1024 * 1024))  # 确保至少为1MB
            self.size_input.setValue(target_size)
            logging.info(f"自动设置目标大小为: {target_size}MB")

    def compress_file(self):
        input_file = self.file_label.text()
        if input_file == '未选择文件':
            self.status_label.setText('请先选择一个文件')
            return

        target_size = self.size_input.value() * 1024 * 1024  # 将MB转换为字节

        self.compress_thread = CompressThread(input_file, target_size)
        self.compress_thread.update_progress.connect(self.update_progress)
        self.compress_thread.compression_done.connect(self.compression_done)
        self.compress_thread.compression_error.connect(self.compression_error)

        self.compress_button.setEnabled(False)
        self.cancel_button.setVisible(True)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.status_label.setText('压缩中...')

        self.compress_thread.start()

    def cancel_compression(self):
        if hasattr(self, 'compress_thread'):
            self.compress_thread.cancel()
        self.status_label.setText('正在取消压缩...')

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def compression_done(self, output_file):
        self.compress_button.setEnabled(True)
        self.cancel_button.setVisible(False)
        self.progress_bar.setVisible(False)
        self.status_label.setText(f'文件已压缩: {output_file}')
        logging.info(f"压缩完成: {output_file}")

    def compression_error(self, error_msg):
        self.compress_button.setEnabled(True)
        self.cancel_button.setVisible(False)
        self.progress_bar.setVisible(False)
        self.status_label.setText(f'压缩失败: {error_msg}')
        logging.error(f"压缩失败: {error_msg}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileCompressor()
    ex.show()
    sys.exit(app.exec_())
