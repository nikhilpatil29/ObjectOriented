from DetailData import *
class StockAccount:
    data = DetailData()
    while True:
        print "-----------------Stock Accounts-----------"
        print "What do you want to perform?"
        print "enter 1.) for add a Customer"
        print "enter 2.) for add a Company"
        print "enter 3.) for display Customer"
        print "enter 4.) for display Company"
        print "enter 5.) for Transaction"
        print "enter 6.) for Exit"

        choice = input("\nEnter your choice")

        if choice == 1:
            data.add_customer()
        elif choice == 2:
            data.add_company()
        elif choice == 3:
            print "---------Total Customer--------"
            data.display_customer()
        elif choice == 4:
            data.display_company()
        elif choice == 5:
            data.tansaction()
        elif choice == 6:
            exit(0)
        else:
            print "You entered a wrong choice! Please re-enter your choice "