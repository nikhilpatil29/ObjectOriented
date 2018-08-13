import datetime
import json
from Customer import *
from Company import *
from Transaction import *
from LinkedListStack import *

customer_info = json.load(open("customer.json","r"))
name_keys = list(customer_info["customers"])
company_info = {}
company_info = json.load(open("company.json","r"))
transaction_obj =  json.load(open("transaction.json","r"))
list_obj = LinkedListStack()

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
            if companylist[data]["company_symbol"] == symbol or companylist[data]["company_name"] == symbol :
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


def buy(amount, noofShares, customer, company,name):

    # print customer["noOfShare"]
    if amount <= company["share_Price"]:

        if noofShares <= customer["noOfShare"]:
            sharePrice = company["share_Price"]     #345
            # print sharePrice
            shares = int(amount)/ int(sharePrice)
            # print ("Shares : " ,shares)
            # print company["share_Price"]

            transaction = Transaction()
            new_customer_amount = int(customer["amount_per_share"]) - int(amount)
            new_no_of_share = int(customer["noOfShare"]) + int(noofShares)
            print "Customer.shares : ",customer["noOfShare"]

            new_company_share= int(company["total_share"]) - int(noofShares)
            # company["share_Price"] = int(company["share_Price"]) - int(amount)

            transaction.set_customer_name(customer["cname"])
            transaction.set_company_symbol(company["company_symbol"])
            transaction.set_buy_sell("Buy")
            transaction.set_total_share(shares)
            transaction.set_total_price(amount)

            now = datetime.datetime.now()
            today =  now.strftime("%Y-%m-%d %H:%M")
            transaction.set_time(today)
            transaction_obj.append({
                "customer_name": transaction.get_customer_name(),
                "company_symbol": transaction.get_company_symbol(),
                "buy_sell": transaction.get_buy_sell(),
                "total_share": transaction.get_total_share(),
                "total_Price": transaction.get_total_price(),
                "time": transaction.get_time()
            })
            # print transaction_obj

            # with open('customer.json', 'r') as file:
            #     json_data = json.load(file)
            name_key = list(customer_info["customers"])
            for item in name_key:
                if item == name:
                    customer_info["customers"][item]["amount_per_share"] = str(new_customer_amount)
                    customer_info["customers"][item]["noOfShare"] = str(new_no_of_share)

                    print ("Person Detail Added Successfully!")

            with open('customer.json', 'w') as data:
                json.dump(customer_info, data)
            name_keys = list(company_info.keys())
            print company_info
            for item in name_keys:
                if item == company["company_name"]:
                    # print  company_info[item]["total_share"]
                    company_info[item]["total_share"] = str(new_company_share)
                    print ("Person Detail Added Successfully!")

            with open('company.json', 'w') as data:
                json.dump(company_info, data)

            with open('transaction.json', 'w') as data:
                json.dump(transaction_obj, data)
def sell(amount, noofShares, customer, company,name):

    # print customer["noOfShare"]
    if noofShares <= customer["noOfShare"]:
        if amount <= company["share_Price"]:
            sharePrice = customer["amount_per_share"]
            # print sharePrice
            shares = int(amount) / int(sharePrice)
            # print ("Shares : " ,shares)
            # print company["share_Price"]

            transaction = Transaction()
            new_customer_amount = int(customer["amount_per_share"]) + int(amount)
            new_no_of_share = int(customer["noOfShare"]) - int(noofShares)
            print "Customer.shares : ",customer["noOfShare"]

            new_company_share= int(company["total_share"]) + int(noofShares)
            # company["share_Price"] = int(company["share_Price"]) - int(amount)

            transaction.set_customer_name(customer["cname"])
            transaction.set_company_symbol(company["company_symbol"])
            transaction.set_buy_sell("Sell")
            transaction.set_total_share(shares)
            transaction.set_total_price(amount)

            now = datetime.datetime.now()
            today =  now.strftime("%Y-%m-%d %H:%M")
            transaction.set_time(today)
            transaction_obj.append(
            {
                "customer_name": transaction.get_customer_name(),
                "company_symbol": transaction.get_company_symbol(),
                "buy_sell": transaction.get_buy_sell(),
                "total_share": transaction.get_total_share(),
                "total_Price": transaction.get_total_price(),
                "time": transaction.get_time()
            })
            # print transaction_obj

            # with open('customer.json', 'r') as file:
            #     json_data = json.load(file)
            name_key = list(customer_info["customers"])
            for item in name_key:
                if item == name:
                    customer_info["customers"][item]["amount_per_share"] = str(new_customer_amount)
                    customer_info["customers"][item]["noOfShare"] = str(new_no_of_share)

                    print ("Person Detail Added Successfully!")

            with open('customer.json', 'w') as data:
                json.dump(customer_info, data)
            name_keys = list(company_info.keys())

            for item in name_keys:
                if item == company["company_name"]:
                    # print  company_info[item]["total_share"]
                    company_info[item]["total_share"] = str(new_company_share)
                    print ("Person Detail Added Successfully!")

            with open('company.json', 'w') as data:
                json.dump(company_info, data)

            with open('transaction.json', 'w') as data:
                json.dump(transaction_obj, data)

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
            buy(amount, noofShares, customer, company,name)
        else:
            print "Customer Not Found"
    else:
        print "Company Not Found"

def sell_share():
    customer_name = raw_input("Enter Customer Name from whom Company wants to sell shares : ")
    customer = searchCustomer(customer_name)

    if customer != None:
        company_name= raw_input("Enter Company name to buy share : ")
        company = searchCompany(company_name)

        if company != None:
            amount = raw_input("Enter amount to buy shares : ")
            noofShares = raw_input("Enter number of shares to buy : ")
            sell(amount, noofShares, customer, company,customer_name)
        else:
            print "Customer Not Found"
    else:
        print "Company Not Found"
class DetailData:
    def display_transaction(self):
        for data in transaction_obj:
            print "customer_name : ",data["customer_name"]
            print "buy or sell : ", data["buy_sell"]
            print "total_share : ", data["total_share"]
            print "total_Price : ", data["total_Price"]
            print "time : ", data["time"],"\n"

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
        # list_obj.push(customer)
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
                break
        print ("Person Detail Added Successfully!")

    def display_customer(self):
        print list_obj.display()
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
            sell_share()
