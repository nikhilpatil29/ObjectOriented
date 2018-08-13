import json

data = json.load(open("JSONData.json", "r"))

class Inventary:
    def __init__(self, name , price , kg, amount, inventary_name):
        self.name = name
        self.price = price
        self.kg = kg
        self.amount = amount
        self.inventary_name = inventary_name

    def maintain(self):
        data["inventary"][self.inventary_name].append({
            "Name": self.name,
            "Price": self.price,
            "Kg": self.kg,
            "amount": self.amount
        })

        print"Name ", self.name
        print"Price ", self.price
        print"Kg  ", self.kg
        print"Total amount ", self.amount

        with open("JSONData.json", "w") as inventary_data:
            json.dump(data, inventary_data, sort_keys=True)

class DataManagement:

    def inventery_detail(inventary_name):
        # data = {}
        # print data
        # if inventary_name in data:
        #     data[inventary_name].append({"name":"nikhil","age":"23"})
        # else:
        #     data[inventary_name] = ([{"name": "nikhil", "age": "23"}])
        # print data
        print "enter the ", inventary_name, "detail.."
        print"Enter the name:"
        name = raw_input()
        # print data["inventary"][inventary_name]
        print"Enter the price:"
        price = input()
        print"Enter how many kg.?"
        kg = input()
        print"The total amount to pay"
        amount = price * kg

        obj = Inventary(name, price, kg, amount, inventary_name)
        obj.maintain()

    while True:
        print "Enter your Choice..."
        print"Enter 1 for Rice"
        print"Enter 2 for pulses"
        print"Enter 3 for wheat"
        print"Enter 4 to Save and Exit"
        choice = input()

        if choice == 1:
            name = "rice"
            inventery_detail(name)

        elif choice == 2:
            name = "pulses"
            inventery_detail(name)
        elif choice == 3:
            name = "wheat"
            inventery_detail(name)
        elif choice == 4:
            print "data saved successfully"
        else:
            print "You have entered a wrong choice"