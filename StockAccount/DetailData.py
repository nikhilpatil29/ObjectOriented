import datetime
import json
from Customer import *
from Company import *
from Transaction import *

customer_info = json.load(open("customer.json","r"))
name_keys = list(customer_info["customers"])
company_info = {}
company_info = json.load(open("company.json","r"))
transaction_obj =  json.load(open("transaction.json","r"))

def save(customer_obj):
    for data in name_keys:

        if customer_info["customers"][data]["cname"] == customer_obj.get_customer_name():
            print "Data already found in Database! Please insert a newly data.\n"
            break
        else:
            customer_info["customers"][customer_obj.get_customer_name()] = ({
                'cname': customer_obj.get_customer_name(),
                'noOfShare': customer_obj.get_noOfShare(),
                'amount_per_share': customer_obj.get_amount(),
            })
            with open('customer.json', 'w') as data:
                json.dump(customer_info, data)
            print ("Person Detail Added Successfully!")


def searchCompany(symbol):
    try:
        companylist = json.load(open('company.json', 'r'))
        name_keys = list(companylist.keys())
        count = 0
        for data in name_keys:
            if companylist[data]["company_symbol"] == symbol:
                count += 1
                company_name = companylist[data]["company_name"]
                company_symbol = companylist[data]["company_symbol"]
                total_share = companylist[data]["total_share"]
                share_Price = companylist[data]["share_Price"]

        new_obj = {
            "company_name": company_name,
            "company_symbol": company_symbol,
            "total_share": total_share,
            "share_Price": share_Price
        }
        if count == 0:
            return None
        else:
            return new_obj

    except SyntaxError:
        print "error in name"


def searchCustomer(name):
    try:
        customerlist = json.load(open('customer.json', 'r'))
        name_keys = list(customerlist["customers"].keys())
        count = 0
        for data in name_keys:
            # print data
            if data == name:
                count += 1
                customername = customerlist["customers"][data]["cname"]
                no_of_share = customerlist["customers"][data]["noOfShare"]
                amount_per_share = customerlist["customers"][data]["amount_per_share"]

        new_obj = {
            "cname": customername,
            "noOfShare": no_of_share,
            "amount_per_share": amount_per_share,
        }
        if count == 0:
            return None
        else:
            return new_obj

    except SyntaxError:
        print "error in name"


def buy(amount, noofShares, customer, company):

    print customer["noOfShare"]
    if amount <= company["share_Price"]:

        if noofShares <= customer["noOfShare"]:
            sharePrice = company["share_Price"]
            # print sharePrice
            shares = int(amount)/ int(sharePrice)
            print ("Shares : " ,shares)
            print company["share_Price"]
            if amount <= company["share_Price"]:
                transaction = Transaction()
                customer["amount_per_share"] = int(customer["amount_per_share"]) +int(amount)
                customer["noOfShare"] = int(customer["noOfShare"]) - int(noofShares)
                print "Customer.shares : ",customer["noOfShare"]

                company["total_share"] = int(company["total_share"]) + int(noofShares)
                company["share_Price"] = int(company["share_Price"]) - int(amount)

                transaction.set_customer_name(customer["cname"])
                transaction.set_company_symbol(company["company_symbol"])
                transaction.set_buy_sell("Buy")
                transaction.set_total_share(shares)
                transaction.set_total_price(amount)

                now = datetime.datetime.now()
                today =  now.strftime("%Y-%m-%d %H:%M")
                transaction.set_time(today)
                transaction_obj[transaction.get_customer_name()] = (
                {
                    "customer_name": transaction.get_customer_name(),
                    "company_symbol": transaction.get_company_symbol(),
                    "buy_sell": transaction.get_buy_sell(),
                    "total_share": transaction.get_total_share(),
                    "total_Price": transaction.get_total_price(),
                    "time": transaction.get_time()
                })
                print transaction_obj
                with open('transaction.json', 'w') as data:
                    json.dump(transaction_obj, data)
                    print ("Person Detail Added Successfully!")


def buy_shares():
    symbol = raw_input("Enter Company Symbol to Buy Shares : ")
    company = searchCompany(symbol)
    if company != None:
        name = raw_input("Enter Customer Name from whom Company wants to buy shares : ")
        customer = searchCustomer(name)
        print customer
        if customer != None:
            amount = raw_input("Enter amount to buy shares : ")
            noofShares = raw_input("Enter number of shares to buy : ")
            buy(amount, noofShares, customer, company)
        else:
            print "Customer Not Found"
    else:
        print "Company Not Found"

class DetailData:

    def add_customer(self):
        # customer_obj = Customer()
        print "Customer Information"
        name = raw_input("enter customer name : ")
        amount = raw_input("enter a amount : ")
        no_Of_Share = raw_input("Enter the Number Of Share : ")
        customer_obj = Customer(name,amount,no_Of_Share)
        customer_obj.set_customer_name(name)
        customer_obj.set_amount(amount)
        customer_obj.set_noOfShare(no_Of_Share)
        # customer = ({
        #     "cname" : customer_obj.get_customer_name(),
        #     "noOfShare": customer_obj.get_noOfShare(),
        #     "amount_per_share": customer_obj.get_amount()
        # })
        save(customer_obj)
    def add_company(self):
        print "Customer Information"
        company_name = raw_input("enter company name : ")
        company_symbol = raw_input("enter a company Symbol : ")
        share_price = raw_input("Enter the Price Of Share : ")
        total_share = raw_input("Enter the total Number Of Share : ")
        company_obj = Company(company_name, company_symbol, share_price,total_share)
        company_obj.set_company_name(company_name)
        company_obj.set_company_symbol(company_symbol)
        company_obj.set_share_price(share_price)
        company_obj.set_total_share(total_share)

        for data in company_info:

            if data == company_obj.get_company_name():
                print "Data already found in Database! Please insert a newly data.\n"
                break
            else:
                company_info[company_obj.get_company_name()] = ({
                    "company_name": company_obj.get_company_name(),
                    "company_symbol": company_obj.get_company_symbol(),
                    "share_Price" : company_obj.get_share_price(),
                    "total_share" : company_obj.get_total_share()
                })
                print company_info
                with open('company.json', 'w') as data:
                    json.dump(company_info, data)
                    print ("Person Detail Added Successfully!")

    def display_customer(self):

        print  "\t\tName\tNoOfShare\tAmount\t"
        for data in name_keys:
            print "\t\t",customer_info["customers"][data]["cname"],"\t\t",\
                customer_info["customers"][data]["noOfShare"],"\t\t",\
                customer_info["customers"][data]["amount_per_share"]
        print "\n"

    def display_company(self):
        print  "\t\tName\tSymbol\tShare Price\t"
        for data in company_info:
            print "\t\t",company_info[data]["company_name"],\
                "\t\t", company_info[data]['company_symbol'], "\t\t", company_info[data]['share_Price']
        print "\n"
    def tansaction(self):
        print "enter 1.)Buy Share"
        print "enter 2.)Sell Share"

        choice = input("Enter your choice : ")

        if choice == 1:
            buy_shares()
        elif choice == 2:
            pass
