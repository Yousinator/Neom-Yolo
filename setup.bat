@echo off
REM Check for Python installation
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python first.
    exit /b 1
)

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
if %ERRORLEVEL% NEQ 0 (
    echo Failed to upgrade pip.
    exit /b 1
)

REM Install packages using pip
echo Installing packages...
python -m pip install opencv-python yt-dlp ultralytics
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install packages.
    exit /b 1
)

echo Packages installed successfully.
pause
