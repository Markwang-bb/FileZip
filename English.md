<h1 align="center">FileZip 📁🔐 </h1>
<div align="center">
<p align="center">
  <a href="./README.md">中文</a>｜
  <a href="./English.md">英文</a>
</p>

> A simple yet powerful desktop application that makes file compression a breeze.


</div>

## ✨ Key Features

- 🗂️ Easy file selection for compression
- 🎯 Custom target compression size
- 🔄 Smart setting: Automatically set target size to half of the original file
- 📊 Real-time compression progress display
- ⏹️ Support for canceling compression operations
- 📝 Detailed compression log recording

## 🚀 How to Use

1. Click the "Select File" button to choose the file you want to compress.
2. Set the target compression size:
   - Manually input the target size (MB)
   - Or check the "Automatically set target size to half of the original file" option
3. Click the "Compress" button to start the compression process.
4. Wait for the compression to complete. The compressed file will be saved in the same directory as the original file.

## 🛠️ Technical Details

- 💻 Written in Python 3
- 🖼️ GUI based on PyQt5
- 🗜️ Compression algorithm uses Python's built-in zipfile module
- 🧵 Multi-threading ensures GUI responsiveness

## 📥 Installation and Running

1. Ensure that Python 3.6 or higher is installed on your system.
2. Install the required dependency:
   ```bash
   pip install PyQt5
   ```
3. Run the application:
   ```bash
   python file_compressor.py
   ```

## ⚠️ Notes

- Compressing large files may take a considerable amount of time. Please be patient.
- Some files may not be compressible to the specified size. The program will get as close as possible to the target size.
- Ensure you have enough disk space to save the compressed file.



## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


