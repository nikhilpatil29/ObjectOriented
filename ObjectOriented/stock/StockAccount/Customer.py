class Customer(object):
    def __init__(self,Customer_name,amount,noOfShare):
        self.__CustomerName = Customer_name
        self.__amount = amount
        self.__noOfShare = noOfShare

    def set_customer_name(self,Customer_name):
        self.__CustomerName = Customer_name

    def set_amount(self,amount):
        self.__amount = amount

    def set_noOfShare(self,noOfShare):
        self.__noOfShare = noOfShare

    def get_customer_name(self):
        return self.__CustomerName

    def get_amount(self):
        return self.__amount

    def get_noOfShare(self):
        return self.__noOfShare