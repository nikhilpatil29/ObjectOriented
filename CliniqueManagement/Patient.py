class Patient():
    """Initialize a new contact object.
    Takes in name and phone number. Other arguments are optional."""
    # def __init__(self, firstname, lastname, patient_number, age):
    #     self.__firstName = firstname.lower()
    #     self.__lastName = lastname.lower()
    #     self.__patientNumber = patient_number
    #     self.__age = age

    def set_first_name(self,first_name):
        self.__firstName = first_name


    def set_last_name(self,last_name):
        self.__lastName = last_name


    def set_patient_id(self, patient_id):
        self.__patientNumber = patient_id

    def set_patient_number(self,patient_number):
        self.__patient_number = patient_number

    def set_age(self,age):
        self.__age = age

    def get_first_name(self):
        return self.__firstName

    def get_last_name(self):
        return self.__lastName

    def get_patient_id(self):
        return self.__patientNumber

    def get_patient_number(self):
        return self.__patient_number

    def get_age(self):
        return self.__age



