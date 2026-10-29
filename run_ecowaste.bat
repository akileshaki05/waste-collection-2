@echo off
echo ======================================================================
echo   ECOWASTE - SMART SYSTEM FOR HOUSEHOLD WASTE COLLECTION
echo   PSG COLLEGE OF TECHNOLOGY - DEPARTMENT OF COMPUTER APPLICATIONS
echo   TEAM NO: 04 (Aishwaryaa S.K, Akilesh N, Ashritaa N | Guide: Dr. Bhama S)
echo ======================================================================
echo.
cd /d "%~dp0"
echo Starting EcoWaste AI Server on http://localhost:5000 ...
python app.py
pause

