@echo off

REM Install dependencies
pip install -r requirements.txt

REM Perform any additional build steps specific to your project

REM Example: Run database migrations
python manage.py migrate

REM Example: Start the application server
python manage.py runserver
