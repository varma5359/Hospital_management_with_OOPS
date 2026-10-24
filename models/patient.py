from .person import Person


class Patient(Person):

    def __init__(
        self,
        name,
        age,
        gender,
        phone,
        patient_id,
        disease,
        doctor,
        nurse
    ):

        # Calling parent constructor
        super().__init__(
            name,
            age,
            gender,
            phone
        )

        self.patient_id = patient_id
        self.disease = disease
        self.doctor = doctor
        self.nurse = nurse

    def add_profile(self):

        return {
            "Patient ID": self.patient_id,
            "Name": self.name,
            "Disease": self.disease,
            "Doctor": self.doctor,
            "Nurse": self.nurse,
            "Phone": self.phone
        }

    def get_data(self):

        data = super().get_data()

        data["Patient ID"] = self.patient_id
        data["Disease"] = self.disease
        data["Doctor"] = self.doctor
        data["Nurse"] = self.nurse

        return data