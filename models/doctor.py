from .person import Person


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

        # Calling parent constructor
        super().__init__(
            name,
            age,
            gender,
            phone
        )

        self.doctor_id = doctor_id
        self.specialization = specialization
        self.experience = experience

    def add_profile(self):

        return {
            "Doctor ID": self.doctor_id,
            "Name": self.name,
            "Specialization": self.specialization,
            "Experience": self.experience,
            "Phone": self.phone
        }

    def get_data(self):

        data = super().get_data()

        data["Doctor ID"] = self.doctor_id
        data["Specialization"] = self.specialization
        data["Experience"] = self.experience

        return data