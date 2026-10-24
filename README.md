# 🏥 Hospital Management System

A beginner-friendly **Hospital Management System** built using **Python Object-Oriented Programming (OOP)** and **Streamlit**.

The main purpose of this project is to understand how real-world entities such as **Doctors, Nurses, Patients, and Prescriptions** can be represented using Python classes and objects.

> **Project Rule:** This project focuses only on Python OOP and Streamlit. No database, Pandas, NumPy, Django, FastAPI, or external backend framework is used.

---

# 📌 1. Project Overview

The Hospital Management System allows hospital staff to:

- Add doctors
- Add nurses
- Add patients
- Assign a doctor to a patient
- Assign a nurse to a patient
- Create prescriptions for patients
- View doctors
- View nurses
- View patients
- View prescriptions
- Display basic hospital statistics

The project is designed to demonstrate how **OOP concepts are used in a practical application**.

---

# 🎯 2. Project Objectives

The main objectives are:

1. Understand classes and objects.
2. Understand constructors using `__init__()`.
3. Understand instance variables using `self`.
4. Understand inheritance.
5. Understand the `super()` method.
6. Understand method creation.
7. Understand method overriding.
8. Understand polymorphism.
9. Understand relationships between objects.
10. Connect OOP classes with a Streamlit UI.
11. Build a small real-world application using Python.

---

# 🧠 3. OOP Concepts Used

| OOP Concept | Project Implementation |
|---|---|
| Class | `Person`, `Doctor`, `Nurse`, `Patient` |
| Object | `doctor`, `nurse`, `patient` |
| Constructor | `__init__()` |
| Instance Variable | `self.name`, `self.age`, etc. |
| Inheritance | `Doctor(Person)` |
| `super()` | Calling `Person.__init__()` |
| Method | `get_data()`, `add_profile()` |
| Method Overriding | Child classes redefine `get_data()` |
| Polymorphism | Different classes use `get_data()` |
| Encapsulation | Data is maintained inside objects |
| Object Relationship | Patient has Doctor and Nurse |
| Composition/Management | Hospital manages multiple objects |

---

# 📁 4. Project Structure

```text
hospital_management/
│
├── app.py
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── doctor.py
│   ├── nurse.py
│   ├── patient.py
│   └── prescription.py
│
├── services/
│   ├── __init__.py
│   └── hospital.py
│
└── requirements.txt
```

---

# 📂 5. Folder Explanation

## `app.py`

This is the main Streamlit application.

It is responsible for:

- Displaying the UI
- Taking user input
- Calling OOP classes
- Creating objects
- Calling methods
- Displaying results

The business objects themselves are defined in the `models` folder.

---

## `models/`

This folder contains the main OOP classes.

```text
models/
│
├── person.py
├── doctor.py
├── nurse.py
├── patient.py
└── prescription.py
```

---

## `services/`

This contains the class responsible for managing the hospital.

```text
services/
└── hospital.py
```

The `Hospital` class manages:

```text
Doctors
Nurses
Patients
Prescriptions
```

---

# 👨‍👩‍👧‍👦 6. Class Architecture

The project uses a parent class called `Person`.

```text
                    Person
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
       Doctor       Nurse      Patient
```

`Doctor`, `Nurse`, and `Patient` are all types of `Person`.

---

# 🏥 7. Hospital Relationship

The `Hospital` class manages the objects.

```text
                     Hospital
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
      Doctors[]      Nurses[]      Patients[]
                                      │
                                      ▼
                                Prescription[]
```

For example:

```text
Hospital
   │
   ├── Doctor 1
   ├── Doctor 2
   │
   ├── Nurse 1
   ├── Nurse 2
   │
   ├── Patient 1
   └── Patient 2
```

---

# 👤 8. Person Class

File:

```text
models/person.py
```

`Person` is the parent class.

It contains common information shared by:

- Doctor
- Nurse
- Patient

Example:

```python
class Person:

    def __init__(self, name, age, gender, phone):

        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def get_data(self):

        return {
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Phone": self.phone
        }
```

Common variables:

```text
name
age
gender
phone
```

---

# 👨‍⚕️ 9. Doctor Class

File:

```text
models/doctor.py
```

Doctor inherits from Person.

```python
class Doctor(Person):
```

Doctor has the common Person information:

```text
name
age
gender
phone
```

and its own information:

```text
doctor_id
specialization
experience
```

Example:

```python
doctor = Doctor(
    "Dr. Ravi",
    45,
    "Male",
    "9876543210",
    "D001",
    "Cardiology",
    15
)
```

The object contains:

```text
Doctor
│
├── name = Dr. Ravi
├── age = 45
├── gender = Male
├── phone = 9876543210
├── doctor_id = D001
├── specialization = Cardiology
└── experience = 15
```

---

# 👩‍⚕️ 10. Nurse Class

File:

```text
models/nurse.py
```

Nurse also inherits from Person.

Common information:

```text
name
age
gender
phone
```

Nurse-specific information:

```text
nurse_id
department
shift
```

Example:

```python
nurse = Nurse(
    "Anitha",
    30,
    "Female",
    "9876501234",
    "N001",
    "Cardiology",
    "Morning"
)
```

---

# 🧑 11. Patient Class

File:

```text
models/patient.py
```

Patient inherits from Person.

Patient-specific information:

```text
patient_id
disease
doctor
nurse
```

Example:

```python
patient = Patient(
    "Ravi",
    30,
    "Male",
    "9876512345",
    "P001",
    "Fever",
    "Dr. Kumar",
    "Anitha"
)
```

The patient therefore has a relationship with:

```text
Patient
   │
   ├── Doctor
   └── Nurse
```

---

# 💊 12. Prescription Class

File:

```text
models/prescription.py
```

The Prescription class stores prescription information.

```text
prescription_id
patient
doctor
medicine
dosage
days
```

Example:

```python
prescription = Prescription(
    "PR001",
    "Ravi",
    "Dr. Kumar",
    "Paracetamol",
    "500mg",
    5
)
```

Relationship:

```text
Patient
   │
   ▼
Prescription
   │
   ├── Medicine
   ├── Dosage
   └── Days
```

---

# 🏢 13. Hospital Class

File:

```text
services/hospital.py
```

The Hospital class manages all objects.

It contains:

```python
self.doctors = []
self.nurses = []
self.patients = []
self.prescriptions = []
```

These are lists containing objects.

For example:

```text
hospital.doctors

[
    doctor1,
    doctor2,
    doctor3
]
```

---

# 🔄 14. How `super()` Works

One of the main objectives of this project is understanding `super()`.

Consider:

```python
class Doctor(Person):

    def __init__(
        self,
        name,
        age,
        gender,
        phone,
        doctor_id,
        specialization,
        experience
    ):

        super().__init__(
            name,
            age,
            gender,
            phone
        )

        self.doctor_id = doctor_id
        self.specialization = specialization
        self.experience = experience
```

The parent class already has:

```python
self.name
self.age
self.gender
self.phone
```

Therefore we don't need to write them again.

Instead:

```python
super().__init__(
    name,
    age,
    gender,
    phone
)
```

calls the constructor of:

```text
Person
```

So:

```text
Doctor
  │
  │ super()
  ▼
Person.__init__()
  │
  ├── name
  ├── age
  ├── gender
  └── phone
```

Then Doctor adds:

```text
doctor_id
specialization
experience
```

---

# 📖 15. How `get_data()` Works

Parent class:

```python
def get_data(self):

    data = {
        "Name": self.name,
        "Age": self.age,
        "Gender": self.gender,
        "Phone": self.phone
    }

    return data
```

The dictionary is created inside `Person.get_data()`.

Doctor:

```python
def get_data(self):

    data = super().get_data()

    data["Doctor ID"] = self.doctor_id
    data["Specialization"] = self.specialization
    data["Experience"] = self.experience

    return data
```

This means:

```text
Doctor.get_data()
       │
       ▼
super().get_data()
       │
       ▼
Person.get_data()
       │
       ▼
Parent dictionary
       │
       ▼
Doctor adds its own information
       │
       ▼
Final dictionary
```

Final result:

```python
{
    "Name": "Dr. Ravi",
    "Age": 45,
    "Gender": "Male",
    "Phone": "9876543210",
    "Doctor ID": "D001",
    "Specialization": "Cardiology",
    "Experience": 15
}
```

---

# 🔀 16. Method Overriding

The parent has:

```python
get_data()
```

Doctor also has:

```python
get_data()
```

Nurse also has:

```python
get_data()
```

Patient also has:

```python
get_data()
```

The child classes override the parent's method.

Example:

```text
Person
  │
  └── get_data()

Doctor
  │
  └── get_data()

Nurse
  │
  └── get_data()

Patient
  │
  └── get_data()
```

This is **method overriding**.

---

# 🔄 17. Polymorphism

Different objects can have the same method name:

```python
doctor.get_data()
nurse.get_data()
patient.get_data()
```

But each object returns its own information.

For example:

```python
doctor.get_data()
```

returns doctor information.

```python
nurse.get_data()
```

returns nurse information.

```python
patient.get_data()
```

returns patient information.

This is a simple practical example of **polymorphism**.

---

# 🔗 18. Patient → Doctor → Nurse Relationship

Suppose we create:

```python
doctor = Doctor(
    "Dr. Kumar",
    45,
    "Male",
    "9876543210",
    "D001",
    "Cardiology",
    15
)
```

And:

```python
nurse = Nurse(
    "Anitha",
    30,
    "Female",
    "9876501234",
    "N001",
    "Cardiology",
    "Morning"
)
```

Then:

```python
patient = Patient(
    "Ravi",
    30,
    "Male",
    "9876512345",
    "P001",
    "Chest Pain",
    doctor,
    nurse
)
```

Now the patient contains the actual objects:

```text
Patient
   │
   ├── Doctor Object
   │       │
   │       ├── ID
   │       ├── Name
   │       ├── Specialization
   │       └── Experience
   │
   └── Nurse Object
           │
           ├── ID
           ├── Name
           ├── Department
           └── Shift
```

This is better OOP modeling than simply storing names.

---

# 💊 19. Prescription Relationship

A prescription belongs to a patient and is issued by a doctor.

```text
Doctor
   │
   │ creates
   ▼
Prescription
   ▲
   │
   │ belongs to
Patient
```

Example:

```text
Patient: Ravi
Doctor: Dr. Kumar

Prescription:
    Medicine: Paracetamol
    Dosage: 500mg
    Days: 5
```

---

# 🖥️ 20. Streamlit Application

The Streamlit application contains the user interface.

The sidebar provides:

```text
Home
Add Doctor
Add Nurse
Add Patient
Create Prescription
View Doctors
View Nurses
View Patients
View Prescriptions
```

---

# 🏠 21. Home Page

The home page displays basic statistics:

```text
Doctors       5
Nurses        8
Patients     20
Prescriptions 15
```

The values are calculated using:

```python
len(hospital.get_doctors())
```

```python
len(hospital.get_nurses())
```

```python
len(hospital.get_patients())
```

```python
len(hospital.get_prescriptions())
```

---

# 👨‍⚕️ 22. Add Doctor Workflow

```text
User
 │
 ▼
Enter Doctor Information
 │
 ▼
Streamlit
 │
 ▼
Doctor(...)
 │
 ▼
Doctor Object
 │
 ▼
hospital.add_doctor()
 │
 ▼
hospital.doctors[]
```

Example:

```text
D001
Dr. Ravi
Cardiology
15 years
```

---

# 👩‍⚕️ 23. Add Nurse Workflow

```text
User
 │
 ▼
Enter Nurse Information
 │
 ▼
Nurse(...)
 │
 ▼
Nurse Object
 │
 ▼
hospital.add_nurse()
 │
 ▼
hospital.nurses[]
```

---

# 🧑 24. Add Patient Workflow

Patient creation depends on doctors and nurses.

```text
Existing Doctors
       │
       ▼
Select Doctor
       │
       │
Existing Nurses
       │
       ▼
Select Nurse
       │
       ▼
Create Patient
       │
       ▼
hospital.add_patient()
```

Example:

```text
Patient
Ravi
P001
Chest Pain

Doctor → Dr. Kumar
Nurse  → Anitha
```

---

# 💊 25. Prescription Workflow

```text
Existing Patients
       │
       ▼
Select Patient
       │
       ▼
Get Doctor
       │
       ▼
Enter Medicine
       │
       ▼
Create Prescription
       │
       ▼
hospital.add_prescription()
```

Example:

```text
Patient: Ravi
Doctor: Dr. Kumar
Medicine: Paracetamol
Dosage: 500mg
Days: 5
```

---

# 🔄 26. Complete Application Flow

```text
                    HOSPITAL
                       │
                       ▼
                 Streamlit UI
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
      Doctor         Nurse         Patient
        │              │              │
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼
                 Prescription
```

---

# 🧩 27. Complete Object Flow

When the application starts:

```python
hospital = Hospital("City Care Hospital")
```

Hospital contains:

```text
doctors = []
nurses = []
patients = []
prescriptions = []
```

After adding a doctor:

```text
doctors = [doctor1]
```

After adding a nurse:

```text
nurses = [nurse1]
```

After adding a patient:

```text
patients = [patient1]
```

After creating a prescription:

```text
prescriptions = [prescription1]
```

So the Hospital object becomes the central manager.

---

# 🛠️ 28. Technologies Used

## Python

Used for:

- Classes
- Objects
- Constructors
- Inheritance
- Methods
- Object relationships

## Streamlit

Used for:

- Forms
- Input fields
- Buttons
- Dropdowns
- Sidebar
- Displaying data
- Dashboard

---

# 🚫 29. Technologies Not Used

This version intentionally does NOT use:

```text
❌ Pandas
❌ NumPy
❌ SQL
❌ MySQL
❌ SQLite
❌ MongoDB
❌ Django
❌ FastAPI
❌ Flask
❌ REST API
```

The purpose is to focus on:

```text
Python OOP + Streamlit
```

---

# ⚙️ 30. Installation

## Step 1: Clone/Create the project

Create:

```text
hospital_management/
```

and create the folders/files according to the project structure.

---

## Step 2: Install Streamlit

Open terminal:

```bash
pip install streamlit
```

Or:

```bash
pip install -r requirements.txt
```

---

# ▶️ 31. Run the Application

From the project root:

```bash
streamlit run app.py
```

Streamlit will open the application in your browser.

---

# 🧪 32. Recommended Testing Order

Test the application in this order:

### Step 1 — Add Doctor

```text
Doctor ID: D001
Name: Dr. Kumar
Specialization: Cardiology
Experience: 15
```

### Step 2 — Add Nurse

```text
Nurse ID: N001
Name: Anitha
Department: Cardiology
Shift: Morning
```

### Step 3 — Add Patient

```text
Patient ID: P001
Name: Ravi
Disease: Chest Pain

Doctor: Dr. Kumar
Nurse: Anitha
```

### Step 4 — Create Prescription

```text
Prescription ID: PR001
Patient: Ravi
Medicine: Paracetamol
Dosage: 500mg
Days: 5
```

### Step 5 — View Data

Check:

```text
View Doctors
View Nurses
View Patients
View Prescriptions
```

---

# 🎓 33. What You Should Be Able to Explain in an Interview

After completing this project, you should be able to explain:

### Question 1

**What is a class?**

A class is a blueprint for creating objects.

Example:

```python
class Doctor:
    pass
```

---

### Question 2

**What is an object?**

An object is an instance of a class.

```python
doctor = Doctor(...)
```

---

### Question 3

**Why do we use `__init__()`?**

`__init__()` initializes the object's data when the object is created.

---

### Question 4

**What is `self`?**

`self` refers to the current object.

```python
self.name = name
```

---

### Question 5

**What is inheritance?**

Inheritance allows a child class to reuse properties and methods from a parent class.

```python
class Doctor(Person):
```

---

### Question 6

**Why do we use `super()`?**

`super()` allows a child class to access the parent class's methods or constructor.

```python
super().__init__(
    name,
    age,
    gender,
    phone
)
```

---

### Question 7

**Where is the dictionary created in `get_data()`?**

The dictionary is created in:

```python
Person.get_data()
```

The child class gets it using:

```python
data = super().get_data()
```

and then adds its own information.

---

### Question 8

**What is method overriding?**

When a child class provides its own implementation of a method already defined in the parent class.

Example:

```text
Person → get_data()

Doctor → get_data()
Nurse → get_data()
Patient → get_data()
```

---

### Question 9

**What is polymorphism in this project?**

Different classes have the same method name:

```python
doctor.get_data()
nurse.get_data()
patient.get_data()
```

but each method returns information specific to that object.

---

# ⚠️ 34. Current Project Limitation

This project does not use a database.

The data is stored in Python objects and lists:

```python
self.doctors = []
self.nurses = []
self.patients = []
self.prescriptions = []
```

Therefore, when the application is completely restarted, the data will be lost.

This is intentional for the **OOP learning version**.

---

# 🚀 35. Future Improvements

After understanding this version, the project can be extended with:

```text
Version 1
─────────
✓ Add Doctor
✓ Add Nurse
✓ Add Patient
✓ Prescription
✓ View Data


Version 2
─────────
→ Search Patient
→ Search Doctor
→ Update Patient
→ Delete Patient
→ Update Doctor
→ Delete Doctor


Version 3
─────────
→ Appointment Management
→ Room Management
→ Billing
→ Patient Medical History


Version 4
─────────
→ Database
→ Login
→ Admin Panel
→ Doctor Panel
→ Nurse Panel


Version 5
─────────
→ AWS Deployment
→ Authentication
→ Production Database
```

---

# 📌 36. Final Architecture

The final architecture is:

```text
                    ┌─────────────────────┐
                    │      Streamlit      │
                    │       app.py        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Hospital       │
                    │      Service        │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
          ┌────────┐       ┌────────┐       ┌─────────┐
          │ Doctor │       │ Nurse  │       │ Patient │
          └────┬───┘       └────┬───┘       └────┬────┘
               │                │                │
               └────────────────┼────────────────┘
                                │
                                ▼
                         ┌──────────────┐
                         │ Prescription │
                         └──────────────┘

Doctor, Nurse and Patient
            │
            ▼
         Person
      (Parent Class)
```

---

# ⭐ 37. Project Summary

This project demonstrates how to build a simple real-world application using Python OOP.

The key idea is:

```text
User
 ↓
Streamlit
 ↓
Create Object
 ↓
Call OOP Method
 ↓
Hospital manages Object
 ↓
Display Object Data
```

The most important OOP relationship is:

```text
Person
  │
  ├── Doctor
  ├── Nurse
  └── Patient
```

And the Hospital manages those objects:

```text
Hospital
  │
  ├── Doctors
  ├── Nurses
  ├── Patients
  └── Prescriptions
```

This keeps the project simple enough for a beginner while demonstrating the core OOP concepts required for a practical Python project.