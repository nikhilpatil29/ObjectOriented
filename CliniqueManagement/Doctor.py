class Doctor():
    """Initialize a new contact object.
    Takes in name and phone number. Other arguments are optional."""
    # def __init__(self, firstname, lastname, id, availability,specification):
    #     self.__firstName = firstname.lower()
    #     self.__lastName = lastname.lower()
    #     self.__id = id
    #     self.__availability = availability
    #     self.__specification = specification

    def set_first_name(self,first_name):
        self.__firstName = first_name

    def set_last_name(self,last_name):
        self.__lastName = last_name

    def set_id(self,id):
        self.__id = id

    def set_availability(self,availability):
        self.__availability = availability

    def set_specification(self,specification):
        self.__specification = specification

    def get_first_name(self):
        return self.__firstName

    def get_last_name(self):
        return self.__lastName

    def get_id(self):
        return self.__id

    def get_specification(self):
        self.__specification

    def get_availability(self):
        return self.__availability




