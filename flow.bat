@echo off
REM Create root directory and navigate into it
REM Create root files
type nul > app.py
type nul > requirements.txt

REM Create models directory and files
mkdir models
type nul > models\__init__.py
type nul > models\person.py
type nul > models\doctor.py
type nul > models\nurse.py
type nul > models\patient.py
type nul > models\prescription.py

REM Create services directory and files
mkdir services
type nul > services\__init__.py
type nul > services\hospital.py

echo Hospital Management project structure created successfully!
pause
