from setuptools import setup

APP = ['file_compressor.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt5'],
    'plist': {
        'CFBundleName': "文件压缩器",
        'CFBundleDisplayName': "文件压缩器",
        'CFBundleGetInfoString': "压缩文件到指定大小",
        'CFBundleIdentifier': "com.yourcompany.FileCompressor",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2023, Your Company, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
