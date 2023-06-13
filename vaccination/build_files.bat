@echo off

REM Install dependencies
pip install -r requirements.txt

REM Collect static files
python manage.py collectstatic --noinput

REM Run database migrations
python manage.py migrate
