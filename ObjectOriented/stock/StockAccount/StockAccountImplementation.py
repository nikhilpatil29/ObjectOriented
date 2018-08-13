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
    customerFile = "customer.json"
    companyFile = "company.json"
    transactionFile = "transaction.json"
    linklist_obj = LinkList()
    transaction_obj = Transaction()

    # /*
    #  * Function to read json data from file
    #  * @param filename
    #  */
    def read_json(self,filename):
        jsonDataObj = json.load(open(filename, "r"))
        return jsonDataObj

    # /*
    #  * Function to save data into json formate in file
    #  * @param data
    #  * @param filename
    #  */
    def save(self,data,filename):
        with open(filename , 'w') as temp:
            json.dump(data, temp)
        print ("Person Detail Added Successfully!")

    # /*
    #  * Function to add customers
    #  */
    def add_customer(self):
        print "Customer Information"
        name = raw_input("enter customer name : ")
        amount = raw_input("enter a amount : ")
        no_Of_Share = raw_input("Enter the Number Of Share : ")
        customer_obj = Customer(name,amount,no_Of_Share)
        customer_obj.set_customer_name(name)
        customer_obj.set_amount(amount)
        customer_obj.set_noOfShare(no_Of_Share)
        customer = self.read_json(self.customerFile)
        customer["customers"].append({
            "cname" : customer_obj.get_customer_name(),
            "noOfShare": customer_obj.get_noOfShare(),
            "amount_per_share": customer_obj.get_amount()
        })
        self.list_obj.push(customer)
        self.save(customer,self.customerFile)

    # /*
    #  * Function to display customers
    #  */
    def display_customer(self):
        customer_data = self.read_json(self.customerFile)
        print  "\t\tName\tNoOfShare\tAmount\t"

        for data in customer_data["customers"]:
            print "\n\t\t",data["cname"],"\t\t", data["noOfShare"],"\t\t",\
                data["amount_per_share"]
        print "\n"

    # /*
    #  * Function to display customers
    #  */
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
        company = self.read_json("company.json")
        company["company"].append({
                "company_name": company_obj.get_company_name(),
                "company_symbol": company_obj.get_company_symbol(),
                "share_Price" : company_obj.get_share_price(),
                "total_share" : company_obj.get_total_share()
                })
        self.list_obj.push(company)
        self.save(company,self.companyFile)

    # /*
    #  * Function to display customers
    #  */
    def display_company(self):
        company_data = self.read_json(self.companyFile)
        print  "\t\tName\tSymbol\tShare Price\t"
        for data in company_data["company"]:
            print "\n\t\t", data["company_name"],"\t\t", data['company_symbol'], "\t\t", \
            data["share_Price"]
        print "\n"

    # /*
    #  * Function to search a companies/customers data
    #  * @param search_data
    #  * @param file
    #  * @param temp
    #  * @return
    #  */
    def search(self, search_data, file, temp):
        try:
            file_data = self.read_json(file)
            count = 0
            if temp == 'company':
                for data in file_data[temp]:
                    if(data["company_symbol"] == search_data or data["company_name"] == search_data):
                        count += 1
                        print "company data found"

                        companyName = data["company_name"]
                        company_symbol = data["company_symbol"]
                        total_share = data["total_share"]
                        share_Price = data["share_Price"]

                        new_obj = {
                            "company_name": companyName,
                            "company_symbol": company_symbol,
                            "total_share": total_share,
                            "share_Price": share_Price
                        }
            else:
                for data in file_data[temp]:
                    if(data["cname"] == search_data):
                        count += 1
                        print "customers data found"

                        customername = data["cname"]
                        no_of_share = data["noOfShare"]
                        amount_per_share = data["amount_per_share"]

                        new_obj = {
                            "cname": customername,
                            "noOfShare": no_of_share,
                            "amount_per_share": amount_per_share
                        }
            if count == 0:
                return None
            else:
                return new_obj

        except SyntaxError:
            print "error in name"

    # /*
    #  * Function to do transaction
    #  */
    def tansaction(self):
        print "enter 1.)Buy Share"
        print "enter 2.)Sell Share"

        choice = input("Enter your choice : ")

        if choice == 1:
            self.buy_shares()
        elif choice == 2:
            self.sell_share()

    # /*
    #  * Function to buy shares
    #  */
    def buy_shares(self):
        symbol = raw_input("Enter Company Symbol to Buy Shares : ")
        company = self.search(symbol,self.companyFile,"company")
        if company != None:
            name = raw_input("Enter Customer Name from whom Company wants to buy shares : ")
            customer = self.search(name, self.customerFile, "customers")
            print customer
            if customer != None:
                amount = raw_input("Enter amount to buy shares : ")
                if customer["amount_per_share"] > 0:
                    print customer["amount_per_share"]
                    noofShares = raw_input("Enter number of shares to buy : ")
                    if company["total_share"] < 0:
                        self.buy(amount, noofShares, customer, company,name)
                    else:
                        print "company shares no left"
                        exit(0)
                else:
                    print "customer has no money"
                    exit(0)
            else:
                print "Customer Not Found"
        else:
            print "Company outer Not Found"

    # /*
    #  * Function to buy stocks
    #  * @param amount
    #  * @param noofShares
    #  * @param customer
    #  * @param company
    #  * @param name
    #  */
    def buy(self,amount, noofShares, customer, company,name):
        print company
        if amount >= company["share_Price"]:
            if noofShares <= customer["noOfShare"]:
                sharePrice = company["share_Price"]
                shares = int(amount) / int(sharePrice)

                new_customer_amount = int(customer["amount_per_share"]) - int(amount)
                new_no_of_share = int(customer["noOfShare"]) + int(noofShares)
                print "Customer.shares : ", customer["noOfShare"]

                new_company_share = int(company["total_share"]) - int(noofShares)
                self.transaction_obj.set_customer_name(customer["cname"])
                self.transaction_obj.set_company_symbol(company["company_symbol"])
                self.transaction_obj.set_buy_sell("Buy")
                self.transaction_obj.set_total_share(str(shares))
                self.transaction_obj.set_total_price(amount)

                now = datetime.datetime.now()
                today = now.strftime("%Y-%m-%d %H:%M")
                self.transaction_obj.set_time(today)
                transaction = self.read_json(self.transactionFile)
                transaction["transaction"].append({
                    "customer_name": self.transaction_obj.get_customer_name(),
                   "company_symbol": self.transaction_obj.get_company_symbol(),
                    "buy_sell": self.transaction_obj.get_buy_sell(),
                    "total_share": self.transaction_obj.get_total_share(),
                    "total_Price": self.transaction_obj.get_total_price(),
                    "time": self.transaction_obj.get_time()
                })

                self.save(transaction,self.transactionFile)
                self.linklist_obj.insertdata(transaction)

                customer_data = self.read_json(self.customerFile)
                for item in customer_data["customers"]:

                    if item["cname"] == name:
                        print "if"
                        print item["amount_per_share"]
                        item["amount_per_share"] = str(new_customer_amount)
                        item["noOfShare"] = str(new_no_of_share)

                        self.save(customer_data, self.customerFile)
                company_data = self.read_json(self.companyFile)

                for item in company_data["company"]:

                    if item["company_name"] == company["company_name"]:
                        item["total_share"] = str(new_company_share)

                        self.save(company_data, self.companyFile)

    # /*
    #  * Function to sell stocks
    #  * @param amount
    #  * @param noofShares
    #  * @param customer
    #  * @param company
    #  * @param name
    #  */
    def sell(self,amount, noofShares, customer, company, name):
        print customer["noOfShare"]
        print noofShares

        if noofShares <= customer["noOfShare"]:
            print "if"
            if amount <= company["share_Price"]:
                sharePrice = customer["amount_per_share"]
                print "if1"
                shares = int(amount) / int(sharePrice)
                print "Shares : " ,shares
                print company["share_Price"]

                new_customer_amount = int(customer["amount_per_share"]) + int(amount)
                new_no_of_share = int(customer["noOfShare"]) - int(noofShares)
                print "Customer.shares : ", customer["noOfShare"]

                new_company_share = int(company["total_share"]) + int(noofShares)

                self.transaction_obj.set_customer_name(customer["cname"])
                self.transaction_obj.set_company_symbol(company["company_symbol"])
                self.transaction_obj.set_buy_sell("Sell")
                self.transaction_obj.set_total_share(str(shares))
                self.transaction_obj.set_total_price(amount)

                now = datetime.datetime.now()
                today = now.strftime("%Y-%m-%d %H:%M")
                self.transaction_obj.set_time(today)
                transaction = self.read_json(self.transactionFile)
                transaction["transaction"].append({
                    "customer_name": self.transaction_obj.get_customer_name(),
                   "company_symbol": self.transaction_obj.get_company_symbol(),
                    "buy_sell": self.transaction_obj.get_buy_sell(),
                    "total_share": self.transaction_obj.get_total_share(),
                    "total_Price": self.transaction_obj.get_total_price(),
                    "time": self.transaction_obj.get_time()
                })
                self.save(transaction, self.transactionFile)
                customer_data = self.read_json(self.customerFile)
                for item in customer_data["customers"]:
                    if item["cname"] == name:
                        item["amount_per_share"] = str(new_customer_amount)
                        item["noOfShare"] = str(new_no_of_share)

                        self.save(customer_data,self.customerFile)
                        print ("Person Detail Added Successfully!")

                company_data = self.read_json(self.companyFile)
                for item in company_data["company"]:
                    if item["company_name"] == company["company_name"]:
                        item["total_share"] = str(new_company_share)
                        self.save(company_data, self.companyFile)
                        print ("Person Detail Added Successfully!")

    # /*
    #  * Function to sell stock
    #  */
    def sell_share(self):
        customer_name = raw_input("Enter Customer Name : ")
        customer = self.search(customer_name,self.customerFile,"customers")

        if customer != None:
            company_name = raw_input("Enter Company name to buy share : ")
            company = self.search(company_name,self.companyFile,"company")

            if company != None:
                amount = raw_input("Enter amount to buy shares : ")
                noofShares = raw_input("Enter number of shares to buy : ")
                self.sell(amount, noofShares, customer, company, customer_name)
            else:
                print "Customer Not Found"
        else:
            print "Company Not Found"

    # /*
    #  * Function to display all transaction
    #  */
    def display_transaction(self):
        transaction_display = self.read_json(self.transactionFile)
        for data in transaction_display["transaction"]:
            print "customer_name : ", data["customer_name"]
            print "buy or sell : ", data["buy_sell"]
            print "total_share : ", data["total_share"]
            print "total_Price : ", data["total_Price"]
            print "time : ", data["time"], "\n"
