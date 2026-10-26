# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py', 'task.py', 'setting.py', r'utils\__init__.py', r'utils\utils.py', r'utils\adb_utils.py', r'utils\POW_handing.py', r'utils\ui2_utils.py', r'utils\wx_ocr.py', 'gui.py'],
    pathex=[r'D:\python_project\All_project\new_venv\.venv\Lib\site-packages'],
    datas=[],
    hiddenimports=['requests', 'gooey', 'lxml', 'shapely', 'pyclipper', 'skimage', 'imgaug', 'imageio', 'fasttext', 'lmdb', 'imghdr', 'fasttext_pybind', 'albumentations', 'docx', 'codecs', 'sys', 'wechat_ocr', 'pathlib', 'functools', 'datetime', 'abc', 'uiautomator2', 'xml'],
    hookspath=['.'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
     a.scripts,
     [],
     exclude_binaries=True,
     name='main',
     debug=False,
     bootloader_ignore_signals=False,
     strip=False,
     upx=True,
     console=False,
	 icon=['D:\\python_project\\All_project\\apk_auto\\auto.ico'])
	 
coll = COLLECT(exe,
     a.binaries,
     a.zipfiles,
     a.datas,
     strip=False,
     upx=True,
     upx_exclude=[],
     name='main')
