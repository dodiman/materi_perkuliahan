@echo off
echo ini adalah runserver yang telah saya buat
echo ini akan dijalankan
pause
cd d:
cd /python39/python38/
cmd /k "venv\scripts\activate.bat & cd materi & python manage.py shell_plus --notebook"