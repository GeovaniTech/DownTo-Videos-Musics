import cx_Freeze

executables = [cx_Freeze.Executable('DownTo.py', icon='View/QRC/Logo.ico', base='Win32GUI')]

cx_Freeze.setup(
    name="DownTo",
    options={'build_exe': {'packages': ['PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'pytube', 'sys', 'os', 'tkinter', 'shutil', 'sqlite3'],
                           'include_files': ['View/', 'bank_DownTo']}},
    executables=executables
)