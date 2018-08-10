from StockReport import *
import json

class Stock:
    def __init__(self,name,no_of_share,share_price,total_price):
        self.__name = name
        self.__no_of_share = no_of_share
        self.__share_price = share_price
        self.__total_price = total_price

    def __str__(self):
        return "Name:{0}\nNo of Share:{1}\nShare Price:{2}\nTotal Price:{3}\n".format(self.__name, self.__no_of_share, self.__share_price,self.__total_price)

def stock_report(name_keys):
    obj = StockReport()
    for data in name_keys:
        name = data["name"]
        obj.set_name(name)
        no_of_share = data["no_of_share"]
        obj.set_no_of_share(no_of_share)
        share_prize = data["share_prize"]
        obj.set_prize(share_prize)
        total_Price = int(no_of_share) * int(share_prize)
        obj.set_total(total_Price)
        contact = Stock(name,no_of_share,share_prize,total_Price)
        print contact
        # print " Stock Data is....."
        # print "Name : ", obj.get_name()
        # print "No_Of_Share : ", obj.get_no_of_share()
        # print "Share Prize : ", obj.get_prize()
        # print "Total Amount : ", obj.get_shareTotal()
        # print "\n"


class StockOperation:

    stock_data = json.load(open("stockReport.json", "r"))
    name_keys = list(stock_data["stock"])
    stock_report(name_keys)