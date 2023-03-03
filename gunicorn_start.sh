#!/bin/bash

# Activate your virtual environment
source C:\Users\shera\OneDrive\Desktop\visual studio\finlizedProjectPD02\venv

# Start Gunicorn
exec gunicorn main.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --access-logfile=-
