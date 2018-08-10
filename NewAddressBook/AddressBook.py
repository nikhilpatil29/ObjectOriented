import json
import os

contact_list = {}

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return "Name:{0}\nEmail address:{1}\nPhone:{2}".format(self.name, self.email, self.phone)

    def change_name(self, name):
        self.name = name

    def change_email(self, email):
        self.email = email

    def change_phone(self, phone):
        self.phone = phone


def display_contacts():
    pass


def search_contact():
    pass


def modify_contact():
    pass


def delete_contact():
    pass


def get_contact_info_from_user():
    try:
        contact_name = raw_input("Enter contact name\n")
        contact_email = raw_input("Enter contact email\n")
        contact_phone = raw_input("Enter contact phone number\n")
        contact = Contact(contact_name, contact_email, contact_phone)
        return contact
    except EOFError as e:
        print "You entered end of file. Contact not added"
        raise e
    except KeyboardInterrupt as e:
        print "Keyboard interrupt. Contact not added"
        raise e


def add_contact():

    contact_list = json.load(open("address_book_file.json", "r"))
    is_file_empty = os.path.getsize("address_book_file.json") == 0 #return True or false
    contact = get_contact_info_from_user()
    if not is_file_empty:
        contact_list[contact.name] = ({
            "name": contact.name,
            "email": contact.email,
            "phone": contact.phone
        })
    else:
        contact_list[contact.name] = ({
            "name":contact.name,
            "email":contact.email,
            "phone":contact.phone
        })
    with open('address_book_file.json', 'w') as data:
        json.dump(contact_list, data)
    print "Contact added"
    # contactlist = {}
    # contactlist['users'] = {}
    # address_book_file = json.load(open("address_book_file.json", "r"))
    # try:
    #     contact = get_contact_info_from_user()
    #     print contact
    #     contactlist["users"] = ([{contact}])
    #     # print address_book_file
    #     with open('address_book_file.json', 'w') as data:
    #         json.dump(contactlist["users"], data)
    #
    #     print "Contact added"
    # except KeyboardInterrupt:
    #     print "Contact not added"
    # except EOFError:
    #     print "Contact not added"

class AddressBook():

    while True:
        print """
        Enter 1 to add a contact
        Enter 2 to browse through contacts
        Enter 3 to delete a contact
        Enter 4 to modify a contact
        Enter 5 to search for contact 
        Enter 0 to quit"""
        # print """
        # ---------------Addressbook Book!---------------------
        # ---------------Would you like to:---------------------
        #
        #             1.) Add a Person Detail
        #             2.) List All Details
        #             3.) Search Person
        #             4.) Edit A Person
        #             5.) Delete A Person
        #             6.) Sort by Last Name
        #             7.) Sort by zip code
        #             8.) Quit Program"""
        choice = input("\nSelect an option: ")

        if choice == 0:
            break
        elif choice == 1:
            add_contact()
        elif choice == 2:
            display_contacts()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            modify_contact()
        elif choice == 5:
            search_contact()
        else:
            print "Incorrect choice. Need to enter the choice again"
