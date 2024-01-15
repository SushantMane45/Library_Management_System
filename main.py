import pymysql
import datetime as dt
import p2 as sql
from Library_management_system.Admin import *
from Library_management_system.books import *
from Library_management_system.students import *
from p2 import perform_db_actions




def menu():
    print("\n\n\n LIBRARY MANAGEMENT SYSTEM")
    print("Select the Option from below:")
    print("\n\tOption 1. BOOK ISSUE")
    print("\tOption 2. BOOK DEPOSIT")
    print("\tOption 3. ADMIN MENU")
    print("\tOption 4. DISPLAY OUT BOOKS")
    print("\tOption 5. EXIT")
    mainchoice = input("Enter your choice from the above: ")
    if mainchoice == "1":
        issue_book(DB_NAME)
        return True
    elif mainchoice == "2":
        return_book(DB_NAME)
        return True
    elif mainchoice == "3":
        adm_cont = True
        while adm_cont:
            adm_cont = adminmenu()
        # Admin menu exited but still in main menu
        menu()
    elif mainchoice == "4":
        check_outbooks(DB_NAME)
        return True
    elif mainchoice == "5":
        return False
    else:
        print("Invalid Option Try Agin!")
        return True

DB_NAME = 'library_prj'
# Creating objects
# creating object of ClassStudents
s1 = Students(DB_NAME)
# creating object of ClassBooks
b1 = Books(DB_NAME)

# calling mainmenu
cont = True
while cont:
    cont = menu()


