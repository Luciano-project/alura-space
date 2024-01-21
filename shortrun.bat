@echo off

if "%VIRTUAL_ENV%"=="" (
    call .\venv\Scripts\activate
)
if %errorlevel% equ 0 (
    if "%1" == "-run" (
        call python manage.py runserver
    ) else if "%1" == "-dea" (
        call .\venv\Scripts\deactivate
    ) else if "%1" == "-mm" (
        call python manage.py makemigrations
    ) else if "%1" == "-m" (
        call python manage.py migrate
    ) else (
        echo "Invalid argument"
    )
) else (
    echo %errorlevel%
)
exit /b