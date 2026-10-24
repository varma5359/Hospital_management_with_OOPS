from .person import Person


class Nurse(Person):

    def __init__(self,name,age,gender,phone,nurse_id,department,shift):

        # Calling parent constructor
        super().__init__(
            name,
            age,
            gender,
            phone
        )

        self.nurse_id = nurse_id
        self.department = department
        self.shift = shift

    def add_profile(self):

        return {
            "Nurse ID": self.nurse_id,
            "Name": self.name,
            "Department": self.department,
            "Shift": self.shift,
            "Phone": self.phone
        }

    def get_data(self):

        data = super().get_data()

        data["Nurse ID"] = self.nurse_id
        data["Department"] = self.department
        data["Shift"] = self.shift

        return data