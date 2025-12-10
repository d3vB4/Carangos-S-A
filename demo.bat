@echo off
REM Carangos S/A - Live Demonstration Script for Windows
REM This script demonstrates the automated testing system

echo.
echo ========================================
echo   CARANGOS S/A - LIVE DEMONSTRATION
echo ========================================
echo.

REM Check Python version
python --version

REM Install dependencies
echo.
echo [1/5] Installing dependencies...
pip install -r requirements.txt

REM Run the automated test robot
echo.
echo [2/5] Running Automated Test Robot...
python tests\test_robot.py

REM Run the live demonstration
echo.
echo [3/5] Starting Live Demo...
python tests\test_live_demo.py

REM Run all tests with the master runner
echo.
echo [4/5] Running Complete Test Suite...
python tests\run_all_tests.py

REM Show test coverage
echo.
echo [5/5] Generating Coverage Report...
pytest tests\ --cov=modules --cov-report=html --cov-report=term

REM Open the presentation page
echo.
echo Opening presentation page...
start apresentacao\index_apresentacao.html

echo.
echo ========================================
echo   DEMO COMPLETE! All systems operational!
echo ========================================
echo.
pause
