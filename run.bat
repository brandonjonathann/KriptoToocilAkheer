@echo off

REM Create a new virtual environment
python -m venv myenv

REM Activate the virtual environment
call myenv\Scripts\activate.bat

REM Install the required libraries from requirements.txt
pip install -r requirements.txt