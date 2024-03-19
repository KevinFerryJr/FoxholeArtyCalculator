@echo off
rem Navigate to your project directory
cd /d "C:\path\to\your\project"

rem Compile the Python script with PyInstaller
pyinstaller --onefile --noconsole calculator/gui.py

rem Pause to see the output before closing the window (optional)
pause