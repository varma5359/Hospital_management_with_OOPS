import streamlit as st

from models.doctor import Doctor
from models.nurse import Nurse
from models.patient import Patient
from models.prescription import Prescription
from services.hospital import Hospital
hospital = Hospital("City Care Hospital")
st.set_page_config(
    page_title="Hospital Management System",
    page_icon="ðŸ¥",
    layout="wide"
)
st.sidebar.title("ðŸ¥ Hospital Management")

menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Home",
        "Add Doctor",
        "Add Nurse",
        "Add Patient",
        "Create Prescription",
        "View Doctors",
        "View Nurses",
        "View Patients",
        "View Prescriptions"
    ]
)
if menu == "Home":

    st.title("ðŸ¥ City Care Hospital")

    st.write(
        "Welcome to Hospital Management System"
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Doctors",
            len(hospital.get_doctors())
        )

    with col2:
        st.metric(
            "Nurses",
            len(hospital.get_nurses())
        )

    with col3:
        st.metric(
            "Patients",
            len(hospital.get_patients())
        )

    with col4:
        st.metric(
            "Prescriptions",
            len(hospital.get_prescriptions())
        )
elif menu == "Add Doctor":

    st.title("ðŸ‘¨â€âš•ï¸ Add Doctor")

    name = st.text_input("Doctor Name")

    age = st.number_input(
        "Age",
        min_value=20,
        max_value=80,
        value=30
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    phone = st.text_input("Phone")

    doctor_id = st.text_input("Doctor ID")

    specialization = st.selectbox(
        "Specialization",
        [
            "Cardiology",
            "Neurology",
            "Orthopedics",
            "Dermatology",
            "Pediatrics",
            "General Medicine"
        ]
    )

    experience = st.number_input(
        "Experience",
        min_value=0,
        max_value=50,
        value=1
    )

    if st.button("Add Doctor"):

        if name and phone and doctor_id:

            doctor = Doctor(
                name,
                age,
                gender,
                phone,
                doctor_id,
                specialization,
                experience
            )

            hospital.add_doctor(doctor)

            st.success(
                "Doctor added successfully!"
            )

        else:

            st.error(
                "Please fill all required fields."
            )
elif menu == "Add Nurse":

    st.title("ðŸ‘©â€âš•ï¸ Add Nurse")

    name = st.text_input("Nurse Name")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=70,
        value=25
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    phone = st.text_input("Phone")

    nurse_id = st.text_input("Nurse ID")

    department = st.selectbox(
        "Department",
        [
            "Cardiology",
            "Neurology",
            "Orthopedics",
            "Emergency",
            "General Medicine"
        ]
    )

    shift = st.selectbox(
        "Shift",
        [
            "Morning",
            "Afternoon",
            "Night"
        ]
    )

    if st.button("Add Nurse"):

        if name and phone and nurse_id:

            nurse = Nurse(
                name,
                age,
                gender,
                phone,
                nurse_id,
                department,
                shift
            )

            hospital.add_nurse(nurse)

            st.success(
                "Nurse added successfully!"
            )

        else:

            st.error(
                "Please fill all required fields."
            )
elif menu == "Add Patient":

    st.title("ðŸ§‘ Add Patient")

    name = st.text_input("Patient Name")

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        value=25
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    phone = st.text_input("Phone")

    patient_id = st.text_input("Patient ID")

    disease = st.text_input("Disease")

    # -----------------------------
    # -----------------------------

    doctors = hospital.get_doctors()

    if doctors:

        doctor_names = []

        for doctor in doctors:
            doctor_names.append(doctor.name)

        selected_doctor = st.selectbox(
            "Select Doctor",
            doctor_names
        )

    else:

        st.warning(
            "Please add a doctor first."
        )

        selected_doctor = None

    # -----------------------------
    # -----------------------------

    nurses = hospital.get_nurses()

    if nurses:

        nurse_names = []

        for nurse in nurses:
            nurse_names.append(nurse.name)

        selected_nurse = st.selectbox(
            "Select Nurse",
            nurse_names
        )

    else:

        st.warning(
            "Please add a nurse first."
        )

        selected_nurse = None

    # -----------------------------
    # -----------------------------

    if st.button("Add Patient"):

        if not name:

            st.error("Enter patient name.")

        elif not phone:

            st.error("Enter phone number.")

        elif not patient_id:

            st.error("Enter patient ID.")

        elif not disease:

            st.error("Enter disease.")

        elif not selected_doctor:

            st.error("Select doctor.")

        elif not selected_nurse:

            st.error("Select nurse.")

        else:

            patient = Patient(
                name,
                age,
                gender,
                phone,
                patient_id,
                disease,
                selected_doctor,
                selected_nurse
            )

            hospital.add_patient(patient)

            st.success(
                "Patient added successfully!"
            )
elif menu == "Create Prescription":

    st.title("ðŸ’Š Create Prescription")

    patients = hospital.get_patients()

    if not patients:

        st.warning(
            "Please add a patient first."
        )

    else:

        patient_names = []

        for patient in patients:
            patient_names.append(patient.name)

        selected_patient = st.selectbox(
            "Select Patient",
            patient_names
        )

        # Find patient object

        patient = None

        for p in patients:

            if p.name == selected_patient:

                patient = p
                break

        st.info(
            f"Doctor: {patient.doctor}"
        )

        st.info(
            f"Nurse: {patient.nurse}"
        )

        prescription_id = st.text_input(
            "Prescription ID"
        )

        medicine = st.text_input(
            "Medicine"
        )

        dosage = st.text_input(
            "Dosage"
        )

        days = st.number_input(
            "Number of Days",
            min_value=1,
            max_value=100,
            value=5
        )

        if st.button("Create Prescription"):

            if not prescription_id:

                st.error(
                    "Enter prescription ID."
                )

            elif not medicine:

                st.error(
                    "Enter medicine."
                )

            elif not dosage:

                st.error(
                    "Enter dosage."
                )

            else:

                prescription = Prescription(
                    prescription_id,
                    patient.name,
                    patient.doctor,
                    medicine,
                    dosage,
                    days
                )

                hospital.add_prescription(
                    prescription
                )

                st.success(
                    "Prescription created successfully!"
                )
elif menu == "View Doctors":

    st.title("ðŸ‘¨â€âš•ï¸ Doctors")

    doctors = hospital.get_doctors()

    if not doctors:

        st.info("No doctors available.")

    else:

        for doctor in doctors:

            with st.expander(
                f"{doctor.doctor_id} - {doctor.name}"
            ):

                data = doctor.get_data()

                st.write(
                    "Doctor ID:",
                    data["Doctor ID"]
                )

                st.write(
                    "Name:",
                    data["Name"]
                )

                st.write(
                    "Age:",
                    data["Age"]
                )

                st.write(
                    "Gender:",
                    data["Gender"]
                )

                st.write(
                    "Specialization:",
                    data["Specialization"]
                )

                st.write(
                    "Experience:",
                    data["Experience"]
                )

                st.write(
                    "Phone:",
                    data["Phone"]
                )
elif menu == "View Nurses":

    st.title("ðŸ‘©â€âš•ï¸ Nurses")

    nurses = hospital.get_nurses()

    if not nurses:

        st.info("No nurses available.")

    else:

        for nurse in nurses:

            with st.expander(
                f"{nurse.nurse_id} - {nurse.name}"
            ):

                data = nurse.get_data()

                st.write(
                    "Nurse ID:",
                    data["Nurse ID"]
                )

                st.write(
                    "Name:",
                    data["Name"]
                )

                st.write(
                    "Age:",
                    data["Age"]
                )

                st.write(
                    "Gender:",
                    data["Gender"]
                )

                st.write(
                    "Department:",
                    data["Department"]
                )

                st.write(
                    "Shift:",
                    data["Shift"]
                )

                st.write(
                    "Phone:",
                    data["Phone"]
                )
elif menu == "View Patients":

    st.title("ðŸ§‘ Patients")

    patients = hospital.get_patients()

    if not patients:

        st.info("No patients available.")

    else:

        for patient in patients:

            with st.expander(
                f"{patient.patient_id} - {patient.name}"
            ):

                data = patient.get_data()

                st.write(
                    "Patient ID:",
                    data["Patient ID"]
                )

                st.write(
                    "Name:",
                    data["Name"]
                )

                st.write(
                    "Age:",
                    data["Age"]
                )

                st.write(
                    "Gender:",
                    data["Gender"]
                )

                st.write(
                    "Disease:",
                    data["Disease"]
                )

                st.write(
                    "Doctor:",
                    data["Doctor"]
                )

                st.write(
                    "Nurse:",
                    data["Nurse"]
                )

                st.write(
                    "Phone:",
                    data["Phone"]
                )
elif menu == "View Prescriptions":

    st.title("ðŸ’Š Prescriptions")

    prescriptions = (
        hospital.get_prescriptions()
    )

    if not prescriptions:

        st.info(
            "No prescriptions available."
        )

    else:

        for prescription in prescriptions:

            data = prescription.get_data()

            with st.expander(
                f"{data['Prescription ID']} - "
                f"{data['Patient']}"
            ):

                st.write(
                    "Prescription ID:",
                    data["Prescription ID"]
                )

                st.write(
                    "Patient:",
                    data["Patient"]
                )

                st.write(
                    "Doctor:",
                    data["Doctor"]
                )

                st.write(
                    "Medicine:",
                    data["Medicine"]
                )

                st.write(
                    "Dosage:",
                    data["Dosage"]
                )

                st.write(
                    "Days:",
                    data["Days"]
                )