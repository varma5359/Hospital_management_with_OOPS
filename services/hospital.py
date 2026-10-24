class Hospital:

    def __init__(self, hospital_name):

        self.hospital_name = hospital_name

        self.doctors = []
        self.nurses = []
        self.patients = []
        self.prescriptions = []

    # -----------------------------
    # -----------------------------

    def add_doctor(self, doctor):

        self.doctors.append(doctor)

    def get_doctors(self):

        return self.doctors

    # -----------------------------
    # -----------------------------

    def add_nurse(self, nurse):

        self.nurses.append(nurse)

    def get_nurses(self):

        return self.nurses

    # -----------------------------
    # -----------------------------

    def add_patient(self, patient):

        self.patients.append(patient)

    def get_patients(self):

        return self.patients

    # -----------------------------
    # -----------------------------

    def add_prescription(self, prescription):

        self.prescriptions.append(prescription)

    def get_prescriptions(self):

        return self.prescriptions