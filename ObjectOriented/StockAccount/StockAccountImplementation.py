"""
/******************************************************************************
 *
 *  Purpose: Program to perform stock operation
 *
 *  @author  Nikhil Patil
 *  @version 1.0
 *  @since
 *
 ******************************************************************************/
 """
import datetime
import json
from Customer import *
from Company import *
from LinkedListStack import *
from Transaction import *
from LinkList import *
class StockAccountImplementation:
    list_obj = LinkedListStack()
    linklist_obj = LinkList()
    customer_info = json.load(open("customer.json", "r"))
    company_info = json.load(open("company.json", "r"))
    transaction_obj = json.load(open("transaction.json", "r"))
    name_keys = list(customer_info["customers"].keys())

    # /*
    #  * Function to save
    #  * @param year
    #  * @return
    #  */
    def save(self,customer,name,choice):
        print "defination"
        print choice

        if choice == 1:
            self.customer_info["customers"][name] = ({
                "cname":customer["cname"],
                "noOfShare":customer["noOfShare"],
                "amount_per_share":customer["amount_per_share"]
            })
        # print customer_info
            with open('customer.json', 'w') as data:
                json.dump(self.customer_info, data)
            print ("Person Detail Added Successfully!")
        else:
            print self.company_info
            self.company_info[name] =({
                "company_name": customer["company_name"],
                "company_symbol": customer["company_symbol"],
                "share_Price" : customer["share_Price"],
                "total_share" : customer["total_share"]
                })

            # print self.company_info
            with open('company.json', 'w') as data1:
                json.dump(self.company_info, data1)
            print ("Person Detail Added Successfully!")

    # def save_transaction(self,name,company,transaction,new_customer_amount,new_no_of_share,new_company_share):
    #     self.transaction_obj = ({
    #         "customer_name": transaction["customer_name"],
    #         "company_symbol":transaction["company_symbol"],
    #         "buy_sell": transaction["buy_sell"],
    #         "total_share": transaction["total_share"],
    #         "total_Price": transaction["total_Price"],
    #         "time": transaction["time"],
    #
    #     })
    #     with open('customer.json', 'r') as file:
    #         json_data = json.load(file)
    #     name_key = list(self.customer_info["customers"])
    #     for item in name_key:
    #         if item == name:
    #             self.customer_info["customers"][item]["amount_per_share"] = str(new_customer_amount)
    #             self.customer_info["customers"][item]["noOfShare"] = str(new_no_of_share)
    #
    #             print ("Person Detail Added Successfully!")
    #
    #     with open('customer.json', 'w') as data:
    #         json.dump(self.customer_info, data)
    #     name_keys = list(self.company_info.keys())
    #     print self.company_info
    #     for item in name_keys:
    #         if item == company["company_name"]:
    #             # print  company_info[item]["total_share"]
    #             self.company_info[item]["total_share"] = str(new_company_share)
    #             print ("Person Detail Added Successfully!")
    #
    #     with open('company.json', 'w') as data:
    #         json.dump(self.company_info, data)
    #
    #     with open('transaction.json', 'w') as data:
    #         json.dump(self.transaction_obj, data)

    def add_customer(self):
        print "Customer Information"
        name = raw_input("enter customer name : ")
        amount = raw_input("enter a amount : ")
        no_Of_Share = raw_input("Enter the Number Of Share : ")
        customer_obj = Customer(name,amount,no_Of_Share)
        customer_obj.set_customer_name(name)
        customer_obj.set_amount(amount)
        customer_obj.set_noOfShare(no_Of_Share)
        name = customer_obj.get_customer_name()

        customer = ({
            "cname" : customer_obj.get_customer_name(),
            "noOfShare": customer_obj.get_noOfShare(),
            "amount_per_share": customer_obj.get_amount()
        })
        self.list_obj.push(customer)
        self.save(customer,name,1)


    def display_customer(self):
        print  "\t\tName\tNoOfShare\tAmount\t"
        self.list_obj.display()

        for data in self.name_keys:
            print "\t\t",self.customer_info["customers"][data]["cname"],"\t\t",\
                self.customer_info["customers"][data]["noOfShare"],"\t\t",\
                self.customer_info["customers"][data]["amount_per_share"]
        print "\n"

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

        name = company_obj.get_company_name()

        company = ({
                "company_name": company_obj.get_company_name(),
                "company_symbol": company_obj.get_company_symbol(),
                "share_Price" : company_obj.get_share_price(),
                "total_share" : company_obj.get_total_share()
                })
        self.list_obj.push(company)
        self.save(company, name,2)

    def display_company(self):
        print  "\t\tName\tSymbol\tShare Price\t"
        for data in self.company_info:
            print "\t\t", self.company_info[data]["company_name"], "\t\t", self.company_info[data]['company_symbol'], "\t\t", \
            self.company_info[data]['share_Price']
        print "\n"

    def tansaction(self):
        print "enter 1.)Buy Share"
        print "enter 2.)Sell Share"

        choice = input("Enter your choice : ")

        if choice == 1:
            self.buy_shares()
        elif choice == 2:
            self.sell_share()

    def buy_shares(self):
        symbol = raw_input("Enter Company Symbol to Buy Shares : ")
        company = self.searchCompany(symbol)
        # print company
        if company != None:
            name = raw_input("Enter Customer Name from whom Company wants to buy shares : ")
            customer = self.searchCustomer(name)
            print customer
            if customer != None:
                amount = raw_input("Enter amount to buy shares : ")
                noofShares = raw_input("Enter number of shares to buy : ")
                self.buy(amount, noofShares, customer, company, name)
            else:
                print "Customer Not Found"
        else:
            print "Company outer Not Found"

    def searchCompany(self,search):
        try:
            companylist = json.load(open('company.json', 'r'))
            name_keys = list(companylist.keys())
            count = 0
            # print name_keys
            for data in name_keys:
                if companylist[data]["company_symbol"] == search or companylist[data]["company_name"] == search:
                    count += 1
                    print "company found"
                    companyName = companylist[data]["company_name"]
                    # print companyName
                    company_symbol = companylist[data]["company_symbol"]
                    total_share = companylist[data]["total_share"]
                    share_Price = companylist[data]["share_Price"]

                    new_obj = {
                        "company_name": companyName,
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

    def searchCustomer(self,name):
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

    def buy(self,amount, noofShares, customer, company, name):
        # print customer["noOfShare"]
        if amount >= company["share_Price"]:
            print "outer if"
            if noofShares <= customer["noOfShare"]:
                sharePrice = company["share_Price"]  # 345
                # print sharePrice
                shares = int(amount) / int(sharePrice)
                # print ("Shares : " ,shares)
                # print company["share_Price"]

                transaction = Transaction()
                new_customer_amount = int(customer["amount_per_share"]) - int(amount)
                new_no_of_share = int(customer["noOfShare"]) + int(noofShares)
                print "Customer.shares : ", customer["noOfShare"]

                new_company_share = int(company["total_share"]) - int(noofShares)
                # company["share_Price"] = int(company["share_Price"]) - int(amount)

                transaction.set_customer_name(customer["cname"])
                transaction.set_company_symbol(company["company_symbol"])
                transaction.set_buy_sell("Buy")
                transaction.set_total_share(shares)
                transaction.set_total_price(amount)

                now = datetime.datetime.now()
                today = now.strftime("%Y-%m-%d %H:%M")
                transaction.set_time(today)
                transact = ({
                    "customer_name": transaction.get_customer_name(),
                   "company_symbol": transaction.get_company_symbol(),
                    "buy_sell": transaction.get_buy_sell(),
                    "total_share": transaction.get_total_share(),
                    "total_Price": transaction.get_total_price(),
                    "time": transaction.get_time()
                })
                # self.linklist_obj.insertdata(transact)
                # self.save_transaction(transact,company,name,new_customer_amount,new_no_of_share,new_company_share)
                self.transaction_obj.append({
                    "customer_name": transaction.get_customer_name(),
                    "company_symbol": transaction.get_company_symbol(),
                    "buy_sell": transaction.get_buy_sell(),
                    "total_share": transaction.get_total_share(),
                    "total_Price": transaction.get_total_price(),
                    "time": transaction.get_time()
                })
                print self.transaction_obj

                with open('customer.json', 'r') as file:
                    json_data = json.load(file)
                name_key = list(self.customer_info["customers"])
                for item in name_key:
                    if item == name:
                        self.customer_info["customers"][item]["amount_per_share"] = str(new_customer_amount)
                        self.customer_info["customers"][item]["noOfShare"] = str(new_no_of_share)

                        print ("Person Detail Added Successfully!")

                with open('customer.json', 'w') as data:
                    json.dump(self.customer_info, data)
                name_keys = list(self.company_info.keys())
                print self.company_info
                for item in name_keys:
                    if item == company["company_name"]:
                        # print  company_info[item]["total_share"]
                        self.company_info[item]["total_share"] = str(new_company_share)
                        print ("Person Detail Added Successfully!")

                with open('company.json', 'w') as data:
                    json.dump(self.company_info, data)

                with open('transaction.json', 'w') as data:
                    json.dump(self.transaction_obj, data)

    def sell(self,amount, noofShares, customer, company, name):
        print customer["noOfShare"]
        print noofShares

        if noofShares <= customer["noOfShare"]:
            print "if"
            if amount >= company["share_Price"]:
                sharePrice = customer["amount_per_share"]
                print "if1"
                shares = int(amount) / int(sharePrice)
                print "Shares : " ,shares
                print company["share_Price"]

                transaction = Transaction()
                new_customer_amount = int(customer["amount_per_share"]) + int(amount)
                new_no_of_share = int(customer["noOfShare"]) - int(noofShares)
                print "Customer.shares : ", customer["noOfShare"]

                new_company_share = int(company["total_share"]) + int(noofShares)
                # company["share_Price"] = int(company["share_Price"]) - int(amount)

                transaction.set_customer_name(customer["cname"])
                transaction.set_company_symbol(company["company_symbol"])
                transaction.set_buy_sell("Sell")
                transaction.set_total_share(str(shares))
                transaction.set_total_price(amount)

                now = datetime.datetime.now()
                today = now.strftime("%Y-%m-%d %H:%M")
                transaction.set_time(today)
                self.transaction_obj.append({
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
                name_key = list(self.customer_info["customers"])
                for item in name_key:
                    if item == name:
                        self.customer_info["customers"][item]["amount_per_share"] = str(new_customer_amount)
                        self.customer_info["customers"][item]["noOfShare"] = str(new_no_of_share)

                        print ("Person Detail Added Successfully!")

                with open('customer.json', 'w') as data:
                    json.dump(self.customer_info, data)
                name_keys = list(self.company_info.keys())

                for item in name_keys:
                    if item == company["company_name"]:
                        # print  company_info[item]["total_share"]
                        self.company_info[item]["total_share"] = str(new_company_share)
                        print ("Person Detail Added Successfully!")

                with open('company.json', 'w') as data:
                    json.dump(self.company_info, data)

                with open('transaction.json', 'w') as data:
                    json.dump(self.transaction_obj, data)

    def sell_share(self):
        customer_name = raw_input("Enter Customer Name : ")
        customer = self.searchCustomer(customer_name)

        if customer != None:
            company_name = raw_input("Enter Company name to buy share : ")
            company = self.searchCompany(company_name)

            if company != None:
                amount = raw_input("Enter amount to buy shares : ")
                noofShares = raw_input("Enter number of shares to buy : ")
                self.sell(amount, noofShares, customer, company, customer_name)
            else:
                print "Customer Not Found"
        else:
            print "Company Not Found"

    def display_transaction(self):
        for data in self.transaction_obj:
            print "customer_name : ", data["customer_name"]
            print "buy or sell : ", data["buy_sell"]
            print "total_share : ", data["total_share"]
            print "total_Price : ", data["total_Price"]
            print "time : ", data["time"], "\n"
