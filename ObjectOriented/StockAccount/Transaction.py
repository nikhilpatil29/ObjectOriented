"""
/******************************************************************************
 *
 *  Purpose: Program to set and get value from transaction data
 *
 *  @author  Nikhil Patil
 *  @version 1.0
 *  @since
 *
 ******************************************************************************/
 """
class Transaction(object):
    # def __init__(self, customer_name, comapany_symbol, buy_sell, total_share, total_price, time):
    #     self.__customerName = customer_name
    #     self.__comapanSymbol = comapany_symbol
    #     self.__buySell = buy_sell
    #     self.__totalShare = total_share
    #     self.__totalPrice = total_price
    #     self.__time = time

    def set_customer_name(self, customer_name):
        self.__customerName = customer_name

    def set_company_symbol(self, comapany_symbol):
        self.__comapanSymbol = comapany_symbol

    def set_buy_sell(self, buy_sell):
        self.__buySell = buy_sell

    def set_total_share(self, total_share):
        self.__totalShare = total_share

    def set_total_price(self, total_price):
        self.__totalPrice = total_price

    def set_time(self, time):
        self.__time = time

    def get_customer_name(self):
        return self.__customerName

    def get_company_symbol(self):
        return self.__comapanSymbol

    def get_buy_sell(self):
        return self.__buySell

    def get_total_share(self,):
        return self.__totalShare

    def get_total_price(self):
        return self.__totalPrice

    def get_time(self):
        return self.__time

