<h1 align="center">FileZip 📁🔐 </h1>
<div align="center">
<p align="center">
  <a href="./README.md">Chinese</a>｜
  <a href="./English.md">English</a>
</p>

> 一款简单而强大的桌面应用程序，让文件压缩变得轻松自如。

</div>



## ✨ 主要特性

- 🗂️ 轻松选择要压缩的文件
- 🎯 自定义目标压缩大小
- 🔄 智能设置：自动将目标大小设为原文件的一半
- 📊 实时压缩进度显示
- ⏹️ 支持取消压缩操作
- 📝 详细的压缩日志记录

## 🚀 如何使用

1. 点击 "选择文件" 按钮，选择要压缩的文件。
2. 设置目标压缩大小：
   - 手动输入目标大小（MB）
   - 或勾选 "自动设置目标大小为原文件的一半" 选项
3. 点击 "压缩" 按钮开始压缩过程。
4. 等待压缩完成，压缩后的文件将保存在原文件同一目录下。

## 🛠️ 技术细节

- 💻 使用 Python 3 编写
- 🖼️ 图形界面基于 PyQt5
- 🗜️ 压缩算法使用 Python 内置的 zipfile 模块
- 🧵 多线程处理确保界面响应性

## 📥 安装与运行

1. 确保您的系统已安装 Python 3.6 或更高版本。
2. 安装所需依赖：
   ```bash
   pip install PyQt5
   ```
3. 运行应用程序：
   ```bash
   python file_compressor.py
   ```

## ⚠️ 注意事项

- 压缩大文件可能需要较长时间，请耐心等待。
- 某些文件可能无法压缩到指定大小，程序会尽可能接近目标大小。
- 请确保有足够的磁盘空间用于保存压缩后的文件。

## 📄 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。
