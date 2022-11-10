@echo off

rem --Download python installer
curl "https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe" -o python-installer.exe

rem --Install python
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 

rem --Refresh Environmental Variables
call RefreshEnv.cmd

rem --Use python, pip
python -m venv env
pip install -r requirements.txt
python manage.py runserver

pause
