@echo off

rem Activate your virtual environment
call C:\Users\shera\OneDrive\Desktop\visual studio\finlizedProjectPD02\venv\Scripts\activate

rem Start Gunicorn
gunicorn main.wsgi:application --bind 0.0.0.0:8000 --workers 3 --log-level=info --access-logfile=-


