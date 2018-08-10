class Company(object):
    def __init__(self, company_name, company_symbol, share_price, total_share):
        self.__companyName = company_name
        self.__companySymbol = company_symbol
        self.__sharePrice = share_price
        self.__totalShare = total_share

    def set_company_name(self, company_name):
        self.__companyName = company_name


    def set_company_symbol(self, company_symbol):
        self.__companySymbol = company_symbol

    def set_share_price(self, share_price):
        self.__sharePrice = share_price

    def set_total_share(self, total_share):
        self.__totalShare = total_share

    def get_company_name(self):
        return self.__companyName

    def get_company_symbol(self):
        return self.__companySymbol

    def get_share_price(self):
        return self.__sharePrice

    def get_total_share(self):
        return self.__totalShare