import sys
from cx_Freeze import setup, Executable

includefiles = "config.json"

build_exe_options = {
    "packages": ["os", "sys", "json", "requests", "PySimpleGUI"],
    "include_files": ["config.json"],
    "excludes": ["tkinter"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Moonraker-Console",
    version = "0.1",
    description = "My GUI application!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("__main__.py", base=base, target_name="Moonraker-Console")]
)