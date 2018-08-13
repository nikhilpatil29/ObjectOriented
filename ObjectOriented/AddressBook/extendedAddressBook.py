import json

contactlist = json.load(open("/home/bridgeit/nikhil/Python_Program/ObjectOriented/AddressBook/contacts.json", 'r'))

class extendedAddressBook:

    def edit_information(data):

        while True:
            print"\t0. Exit to main page"
            print"\t1. Edit Address "
            print"\t2. Edit City "
            print"\t3. Edit State "
            print"\t4. Edit ZIP Code "
            print"\t5. Edit Phone Number\n"
            choice = input()

            # contactlist = json.load(open("contacts.json", 'r'))
            # print contactlist["users"][data]["address"]

            if choice == 0:
                return
            elif choice == 1:

                new_address = raw_input("enter a new address:\n")
                contactlist["users"][data]["address"] = new_address
                print contactlist["users"][data]["address"]
                json.dump(contactlist, open("contacts.json", 'w'))

            elif choice == 2:
                # contactlist = json.load(open("contacts.json", 'r'))
                new_city = raw_input("enter a new city:\n")
                contactlist["users"][data]["city"] = new_city
                print contactlist["users"][data]["city"]
                json.dump(contactlist, open("contacts.json", 'w'))

            elif choice == 3:
                # contactlist = json.load(open("contacts.json", 'r'))
                new_state = raw_input("enter a new State:\n")
                contactlist["users"][data]["state"] = new_state
                print contactlist["users"][data]["state"]
                json.dump(contactlist, open("contacts.json", 'w'))

            elif choice == 4:
                # contactlist = json.load(open("contacts.json", 'r'))
                new_zip = raw_input("enter a new ZIP code:\n")
                contactlist["users"][data]["zip"] = new_zip
                print contactlist["users"][data]["zip"]
                json.dump(contactlist, open("contacts.json", 'w'))

            elif choice == 5:
                # contactlist = json.load(open("contacts.json", 'r'))
                new_phone = raw_input("enter a new city:\n")
                contactlist["users"][data]["phone"] = new_phone
                print contactlist["users"][data]["phone"]
                json.dump(contactlist, open("contacts.json", 'w'))

            else:
                print "you have entered wrong choice"

    def checkname(edit_word, data, contactlist):
        if edit_word == contactlist["users"][data]["first_name"]:
            print "word found"
            return True
        else:
            return False


    # contactlist = json.load(open('/home/bridgeit/nikhil/Python_Program/ObjectOriented/AddressBook/contacts.json', 'r'))

    def sortByLastName():
        contactlist = json.load(open('contacts.json', 'r'))
        name_keys = list(contactlist["users"].keys())
        temp = []
        for data in name_keys:
            temp1 = (contactlist["users"][data]["last_name"], data)
            temp.append(temp1)
            temp = sorted(temp)
        print '\tFIRSTNAME\t', 'LASTNAME\t', 'CITY\t', '    PHONE\t', '   STATE\t'
        for i in range(len(temp)):
            key = temp[i][1]
            # print contactlist['users'][key]
            name_keys = list(contactlist["users"].keys())

            print "\t", contactlist["users"][key]['first_name'], "     ", contactlist["users"][key][
                "last_name"], "     ", contactlist["users"][key]["city"], "      ", contactlist["users"][key][
                "phone"], "\t", contactlist["users"][key]["state"], "      "

            # prin7t sortByProperty(contactlist["users"][data]["last_name"])  # sorted_list = sorted(contactlist["users"][data]["last_name"], key=lambda x: (contactlist["users"][x]['last_name'], contactlist["users"][x]['zip']))  # print contactlist["users"][data]["last_name"]  # print contactlist

    def sortByZip():
        contactlist = json.load(open('contacts.json', 'r'))
        name_keys = list(contactlist["users"].keys())
        temp = []
        for data in name_keys:
            temp1 = (contactlist["users"][data]["zip"], data)
            temp.append(temp1)
            temp = sorted(temp)

        for i in range(len(temp)):
            key = temp[i][1]
            print contactlist["users"][key]

            # print key  # value = contactlist['users'][key]  # print value  # contactlist["users"][key] = value  # print(value)  #  # print contactlist.append(value)  # dict.append(value)  # contactlist  # print dict

        exit()

    def save(contactlist):

        with open('/home/bridgeit/nikhil/Python_Program/ObjectOriented/AddressBook/contacts.json', 'w') as data:
            json.dump(contactlist, data)
