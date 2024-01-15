import datetime as dt
import p2 as sql
from p2 import perform_db_actions

class Students:
    def __init__(self, dbname):
        self.dbname = dbname

    def create_student(self):
        name = input("Enter the name of the student: ")
        email = input("Enter the email id of the student: ")
        phone = input("Enter the phone of the student: ")
        q1 = '''INSERT INTO STUDENTS(NAME,EMAIL,PHONE) 
        VALUES('%s','%s','%s')''' % (name, email, phone)
        sql.perform_db_actions(self.dbname, q1)
        print("Successfully added Student record to the database")

    def display_all(self):
        q1 = '''select * from students'''
        rows = sql.perform_db_actions(self.dbname, q1)
        print("Students in the database:")
        for r1 in rows:
            print(r1)

    def display_specific(self):
        memid = int(input("Enter the Membership ID of the the student: "))
        q1 = '''select * from students where memid = %d''' % (memid)
        rows = sql.perform_db_actions(self.dbname, q1)
        print("Details are:")
        for r1 in rows:
            print(r1)

    def modify_student(self):
        memid = int(
            input("Enter the Membership ID of the the student record to be updated: "))
        q1 = '''select name,email,phone from students where memid = %d''' % memid
        rows = sql.perform_db_actions(self.dbname, q1)
        cols = ["Name", "Email", "Phone"]
        q1 = "Update students set "

        if len(rows[0]) > 1:
            for i in range(len(cols)):
                print(f"Current {cols[i]} is {rows[0][i]}")
                ch = input("Enter y to modify: ")
                if ch == 'y':
                    inp = input("Enter the new "+cols[i]+": ")
                    q1 = q1 + cols[i]+" = '"+inp+"',"

            if len(q1) > 23:
                q1 = q1[:-1] + " where memid = "+str(memid)
                rows = sql.perform_db_actions(
                    self.dbname, q1)
                print("Data has been updated")
            else:
                print("Nothing to update!")
        else:
            print("No such data available !")

    def delete_student(self):
        memid = int(
            input("Enter the Membership ID of the student record to be deleted: "))
        q1 = '''select memid from students where memid = %d''' % (memid)
        rows = sql.perform_db_actions(self.dbname, q1)
        if len(rows[0]) >= 1:
            q1 = '''Delete from students where memid = %d''' % (memid)
            rows = sql.perform_db_actions(self.dbname, q1)
            print("Data deleted")
        else:
            print("No such data available!")
