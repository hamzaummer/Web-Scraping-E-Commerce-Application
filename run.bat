@echo off
echo Starting E-commerce Web Scraper...
echo ================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

REM Check if app.py exists
if not exist "app.py" (
    echo Error: app.py not found!
    echo Make sure you're running this from the project directory.
    pause
    exit /b 1
)

REM Run the application
echo Starting the web application...
python run.py

pause
