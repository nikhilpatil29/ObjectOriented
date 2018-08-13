class BookDetail:
    # def __init__(self,firstname,lastname,address,city,state,zip_code,phone_no):
    #     self.__firstname = firstname
    #     self.__lastname = lastname
    #     self.__address = address
    #     self.__city = city
    #     self.__state = state
    #     self.__zip_code = zip_code
    #     self.__phone_no = phone_no

    def set_first_name(self,firstname):
        self.__firstname = firstname

    def set_last_name(self,lastname):
        self.__lastname = lastname

    def set_address(self,address):
        self.__address = address

    def set_city(self,city):
        self.__city = city

    def set_state(self,state):
        self.__state = state

    def set_zip_code(self,zip_code):
        self.__zip_code = zip_code

    def set_phone_no(self,phone_no):
        self.__phone_no = phone_no

    def get_first_name(self):
        return self.__firstname

    def get_last_name(self):
        return self.__lastname

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_phone_no(self):
        return self.__phone_no
