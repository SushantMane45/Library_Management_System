from Library_management_system.main import s1, b1


def adminmenu():
    print("\n\nADMIN MENU")
    print("Select the Option from below:")
    print("\n\tAdmin 1. CREATE STUDENT")
    print("\tAdmin 2. DISPLAY ALL STUDENTS")
    print("\tAdmin 3. DISPLAY SPECIFIC STUDENT")
    print("\tAdmin 4. MODIFY STUDENT RECORD")
    print("\tAdmin 5. DELETE STUDENT RECORD")
    print("\n\tAdmin 6. CREATE BOOK")
    print("\tAdmin 7. DISPLAY ALL BOOKS")
    print("\tAdmin 8. DISPLAY SPECIFIC BOOK")
    print("\tAdmin 9. MODIFY BOOK RECORD")
    print("\tAdmin 10. DELETE BOOK RECORD")
    print("\tAdmin 11. TAKE BACK TO THE MAIN MENU")
    adminchoice = input("Enter your choice from the above: ")
    if adminchoice == "1":
        s1.create_student()
        return True
    elif adminchoice == "2":

        s1.display_all()
        return True
    elif adminchoice == "3":
        s1.display_specific()
        return True
    elif adminchoice == "4":
        s1.modify_student()
        return True
    elif adminchoice == "5":
        s1.delete_student()
        return True
    elif adminchoice == "6":
        b1.create_book()
        return True
    elif adminchoice == "7":
        b1.display_all()
        return True
    elif adminchoice == "8":
        b1.display_specific()
        return True
    elif adminchoice == "9":
        b1.modify_book()
        return True
    elif adminchoice == "10":
        b1.delete_book()
        return True
    elif adminchoice == "11":
        return False
    else:
        print("Invalid Choice. Try again!")
        return True