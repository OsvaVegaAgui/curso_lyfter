class GeneralData:
    def __init__(self):
        self.general = [{'id': 6, 'name': 'Osvaldo', 'age': 34, 'email': 'osvaldo.vega.aguilar@gmail.com'}]

class MedicalHistory:
    def __init__(self):
        self.history = [
            {'date': '01/January/2024', 'subject': 'General check-up', 'patient_id': 6},
            {'date': '23/April/2025', 'subject': 'Back pain', 'patient_id': 6}
        ]

class AuthorizedPerson:
    def __init__(self):
        self.authorized = [{'name': 'Karla', 'phone': '8540-99-10', 'patient_id': 6}]

class Patient(GeneralData, MedicalHistory, AuthorizedPerson):

    def __init__(self, id):
        GeneralData.__init__(self)
        MedicalHistory.__init__(self)
        AuthorizedPerson.__init__(self)
        self.id = id

    def show_patient(self):

        print("Patient Information")
        for patient in self.general:
            if patient['id'] == self.id:
                print(f"Name: {patient['name']}")
                print(f"Age: {patient['age']} \n")

        print("Authorized Contact")
        for person in self.authorized:
            if person['patient_id'] == self.id:
                print(f"Name: {person['name']}")
                print(f"Phone: {person['phone']} \n")

        print("\n **** Medical History ***\n")
        for record in self.history:
            if record['patient_id'] == self.id:
                print(f"Date: {record['date']}")
                print(f"Subject: {record['subject']} \n")


patient1 = Patient(6)
patient1.show_patient()
