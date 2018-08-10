import json
from BookDetail import *
contactlist = json.load(open("/home/bridgeit/nikhil/Python_Program/ObjectOriented/AddressBook/contacts.json", 'r'))
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
            save(contactlist)

        elif choice == 2:
            new_city = raw_input("enter a new city:\n")
            contactlist["users"][data]["city"] = new_city
            print contactlist["users"][data]["city"]
            save(contactlist)

        elif choice == 3:
            new_state = raw_input("enter a new State:\n")
            contactlist["users"][data]["state"] = new_state
            print contactlist["users"][data]["state"]
            save(contactlist)

        elif choice == 4:
            new_zip = raw_input("enter a new ZIP code:\n")
            contactlist["users"][data]["zip"] = new_zip
            print contactlist["users"][data]["zip"]
            save(contactlist)

        elif choice == 5:
            new_phone = raw_input("enter a new city:\n")
            contactlist["users"][data]["phone"] = new_phone
            print contactlist["users"][data]["phone"]
            save(contactlist)

        else:
            print "you have entered wrong choice"


def checkname(edit_word,data,contactlist):
    if edit_word == contactlist["users"][data]["first_name"]:
        print "word found"
        return True
    else:
        return False

# contactlist = json.load(open('/home/bridgeit/nikhil/Python_Program/ObjectOriented/AddressBook/contacts.json', 'r'))
def sortByLastName():
    # contactlist = json.load(open('contacts.json', 'r'))
    name_keys = list(contactlist["users"].keys())
    temp = []
    for data in  name_keys:
        temp1 = (contactlist["users"][data]["last_name"],data)
        temp.append(temp1)
        temp = sorted(temp)
    print '\tFIRSTNAME\t', 'LASTNAME\t', 'CITY\t', '    PHONE\t', '   STATE\t'
    for i in range(len(temp)):
        key = temp[i][1]
        # print contactlist['users'][key]
        name_keys = list(contactlist["users"].keys())



        print "\t", contactlist["users"][key]['first_name'], "     ", contactlist["users"][key]["last_name"], "     ", \
        contactlist["users"][key]["city"], "      ", contactlist["users"][key]["phone"], "\t", \
        contactlist["users"][key]["state"], "      "

        # prin7t sortByProperty(contactlist["users"][data]["last_name"])
        # sorted_list = sorted(contactlist["users"][data]["last_name"], key=lambda x: (contactlist["users"][x]['last_name'], contactlist["users"][x]['zip']))
        # print contactlist["users"][data]["last_name"]
    # print contactlist


def sortByZip():
    # contactlist = json.load(open('contacts.json', 'r'))
    name_keys = list(contactlist["users"].keys())
    temp = []
    for data in  name_keys:
        temp1 = (contactlist["users"][data]["zip"],data)
        temp.append(temp1)
        temp = sorted(temp)

    for i in range(len(temp)):
        key = temp[i][1]
        print contactlist["users"][key]

        # print key
        # value = contactlist['users'][key]
        # print value
        # contactlist["users"][key] = value
        # print(value)
        #
        # print contactlist.append(value)
        # dict.append(value)
        # contactlist
        # print dict

    exit()
def edit_contact():
    try:
        contactlist = json.load(
            open('/home/bridgeit/nikhil/Python_Program/ObjectOriented/AddressBook/contacts.json', 'r'))
        name_keys = list(contactlist["users"].keys())
        edit_word = raw_input("Enter firstname of person to edit contact: ")
        for data in name_keys:
            result = checkname(edit_word, data, contactlist)
            if result:
                edit_information(data)
    except:
        print "error to load a json file"

def save(contactlist):
    with open('/home/bridgeit/nikhil/Python_Program/ObjectOriented/AddressBook/contacts.json', 'w') as data:
        json.dump(contactlist, data)


def delete_a_person():
    contactname = raw_input("Enter Person Name: ")
    contactlist = json.load(open('/home/bridgeit/nikhil/Python_Program/ObjectOriented/AddressBook/contacts.json', 'r'))
    name_keys = list(contactlist["users"].keys())
    # print name_keys
    for data in name_keys:
        if contactlist["users"][data]["first_name"] == contactname:
            contactlist["users"].pop(contactname)
            print "data deleted successfully"


def insert_a_data(obj):
    name_keys = list(contactlist["users"].keys())
    # print name_keys

    try:
        first_name = raw_input("Enter first name: ")
        obj.set_first_name(first_name)
        last_name = raw_input("Enter last name: ")
        obj.set_last_name(last_name)
        address = raw_input("enter the address: ")
        obj.set_address(address)
        city = raw_input("enter the city: ")
        obj.set_city(city)
        state = raw_input("enter the state: ")
        obj.set_state(state)
        zip_code = raw_input("enter the zip code: ")
        obj.set_zip_code(zip_code)
        phone_no = raw_input("Enter phone Number: ")
        obj.set_phone_no(phone_no)

        for data in name_keys:
            if contactlist["users"][data]["phone"] == phone_no:
                print "Data already found in Database! Please insert a newly data.\n"
                break
            else:
                contactlist['users'][first_name] = (
                {'first_name': obj.get_first_name(), 'last_name': obj.get_last_name(), 'address': obj.get_address(),
                    'city': obj.get_city(), 'state': obj.get_state(), 'zip': obj.get_zip_code(), 'phone': obj.get_phone_no()})
                save(contactlist)
                print ("Person Detail Added Successfully!")
    except (NameError, SyntaxError):
        print "Please enter a proper formated data only !"


def search_list(search):

    for data in contactlist["users"]:
        # print contactlist[data]["first_name"]
        if data == search:
            #     print "Data Found"

            # print '\tFIRSTNAME\t', 'LASTNAME\t', 'CITY\t', 'PHONE\t', 'STATE\t'
            # print "\t", contactlist["users"][data]["first_name"], "\t", contactlist["users"][data]["last_name"], "\t", \
            #     contactlist["users"][data]["city"], "\t", contactlist["users"][data]["phone"], "\t", \
            #     contactlist["users"][data]["state"]
            print "First_Name: {0}\nLast_Name: {1}\nPhone: {2}".format(contactlist["users"][data]["first_name"],
                                                                    contactlist["users"][data]["last_name"],
                                                                    contactlist["users"][data]["phone"])

            break


    else:
        print "Data Not found. Please insert a data first."


class PersonDetail:

    obj = BookDetail()
    # Creates an empty list of contacts
    contactlist = {}
    contactlist['users'] = {}
    contactlist = json.load(open('/home/bridgeit/nikhil/Python_Program/ObjectOriented/AddressBook/contacts.json', 'r'))

    while True:
        print """
---------------Addressbook Book!---------------------
---------------Would you like to:---------------------

            1.) Add a Person Detail
            2.) List All Details
            3.) Search Person
            4.) Edit A Person
            5.) Delete A Person
            6.) Sort by Last Name
            7.) Sort by zip code
            8.) Quit Program"""

        userInput = raw_input("\nSelect an option: ")

        if userInput == "1":
            insert_a_data(obj)

         # 2 : list of contacts in addressbook
        elif userInput == "2":
            print "\nListing Contacts...\n"
            name_keys = list(contactlist["users"].keys())
            print "%30s",'\tFIRSTNAME\t', 'LASTNAME\t', 'CITY\t', 'PHONE\t', 'STATE\t'
            for data in name_keys:
                print "\t",contactlist["users"][data]['first_name'],"\t",contactlist["users"][data]["last_name"],"\t",contactlist["users"][data]["city"],"\t",contactlist["users"][data]["phone"],"\t", contactlist["users"][data]["state"],"\t"

        #  3 : search through contacts!
        elif userInput == "3":
            print "\nSearching Contacts..."

            # contactlist = json.load(open('/home/bridgeit/nikhil/Python_Program/ObjectOriented/AddressBook/contacts.json','r'))
            # name_keys = list(contactlist["users"].keys())
            # print name_keys
            # print "All Name's:"
            # for name in name_keys:
            #     print "\t\t\t",name
            search = raw_input("Please enter name: ")

            # print contactlist["users"]
            search_list(search)


        #4 : Edit a contact!
        elif userInput == "4":
            print ("\nEditing Contact...")
            edit_contact()

        #  5 : Delete contact
        elif userInput == "5":
            print ("Deleting a Person...")
            delete_a_person()
            save(contactlist)

        # 6 : Sort By Name
        elif userInput == "6":
            print "Sort Data by Last Name "
            sortByLastName()

        # 6 : Sort By Zip
        elif userInput == '7':
            sortByZip()

        # 6 : end program
        elif userInput == "8":
            print "All Person detail added successfully."
            exit(0)
        else:
            print "Invalid Input! Try again."

