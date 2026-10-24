class Prescription:

    def __init__(
        self,
        prescription_id,
        patient,
        doctor,
        medicine,
        dosage,
        days
    ):

        self.prescription_id = prescription_id
        self.patient = patient
        self.doctor = doctor
        self.medicine = medicine
        self.dosage = dosage
        self.days = days

    def get_data(self):

        return {
            "Prescription ID": self.prescription_id,
            "Patient": self.patient,
            "Doctor": self.doctor,
            "Medicine": self.medicine,
            "Dosage": self.dosage,
            "Days": self.days
        }