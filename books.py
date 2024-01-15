import pymysql
import datetime as dt
import p2 as sql
from p2 import perform_db_actions


class Books:
    def __init__(self, dbname):
        self.dbname = dbname

    def create_book(self):
        title = input("Enter the Title of the Book: ")
        author = input("Enter the Author name of the Book: ")
        publisher = input("Enter the Publisher of the Book: ")
        price = float(input("Enter the Price id of the Book: "))
        copies = int(input("Enter the Copies of the Book: "))

        q1 = '''INSERT INTO BOOKS(title,author,publisher,price,copies) 
        VALUES('%s','%s','%s',%d,%d)''' % (title, author, publisher, price, copies)
        sql.perform_db_actions(self.dbname, q1)
        print("Successfully added book record to the database")

    def display_all(self):
        q1 = '''select * from books'''
        rows = sql.perform_db_actions(self.dbname, q1)
        print("Books available in the Library are:")
        for r1 in rows:
            print(r1)

    def display_specific(self):
        bid = int(input("Enter the ID of the Book: "))
        q1 = '''select * from books where bookid = "%d"''' % (bid)
        rows = sql.perform_db_actions(self.dbname, q1)
        print("Details are:")
        for r1 in rows:
            print(r1)

    def modify_book(self):
        bid = int(input("Enter the ID of the book record to be updated: "))
        q1 = '''select title,author,publisher,price,copies from books 
        where bookid = %d''' % (bid)
        rows = sql.perform_db_actions(self.dbname, q1)
        cols = ['title', 'author', 'publisher', 'price', 'copies']

        q1 = "Update Books set "

        if len(rows[0]) > 1:
            for i in range(len(cols)):
                print(f"Current {cols[i]} is {rows[0][i]}")
                ch = input("Enter y to modify: ")
                if ch == 'y' and i <= 2: #string values
                    inp = input("Enter the new "+cols[i]+": ")
                    q1 = q1 + cols[i]+" = '"+inp+"',"
                if ch == 'y' and i > 2:  #numeric values
                    inp = int(input("Enter the new "+cols[i]+": "))
                    q1 = q1 + cols[i]+" = "+str(inp)+","
            if len(q1) > 18:
                q1 = q1[:-1] + " where bookid = "+str(bid)
                #print("Q1 query = ", q1)
                rows = sql.perform_db_actions(
                    self.dbname, q1)
                print("Data has been updated")
            else:
                print("Nothing to update!")
        else:
            print("No such data available !")

    def delete_book(self):
        bid = int(input("Enter the ID of the Book record to be deleted: "))
        q1 = '''select bookid from books where bookid = %d''' % bid
        rows = sql.perform_db_actions(self.dbname, q1)
        if len(rows[0]) >= 1:
            q1 = '''Delete from Books where bookid = %d''' % bid
            rows = sql.perform_db_actions(self.dbname, q1)
            print("Data deleted")
        else:
            print("No such data available!")

def check_outbooks(db_name):
    print("Borrowed list of books:")
    heading = ('TransactionID', 'Member ID', 'Book ID', 'Issue Date')
    print(heading)
    q1 = '''Select tid,memid,bookid,issue_date from transactions where return_date is null'''
    rows = sql.perform_db_actions(db_name, q1)
    if rows == 0:
        print("No books is pending for returning")
    else:
        for r1 in rows:
            print(r1)

def issue_book(db_name):
    memid = int(input("Enter the Member ID: "))
    bookid = int(input("Enter the Book ID: "))
    book_count = -1

    # checking if MEMID in the database
    q1 = '''Select MEMID from Students where MEMID = %d''' % (memid)
    row1 = sql.perform_db_actions(db_name, q1)

    # checking if BOOKID in the database and if yes then get the count
    q1 = '''Select Copies from Books where bookid = %d''' % (bookid)
    row2 = sql.perform_db_actions(db_name, q1)

    if len(row1) < 1 or len(row2) < 1:
        print("Error: Either BookID or Membership ID is missing, please check and re-try again!")
    elif row2[0][0] < 1:
        print("Error: There are no more copies left in the library!")

    else:
        print("Adding data....")
        #print("   ========    ", datetime.now().strftime('%d-%m-%Y'))
        book_count = row2[0][0]
        q2 = '''INSERT INTO TRANSACTIONS(MEMID,BOOKID,ISSUE_DATE) 
        VALUES(%d,%d,'%s')''' % (memid, bookid, str(dt.datetime.now().strftime('%Y-%m-%d')))
        sql.perform_db_actions(db_name, q2)

        # update the copies
        q2 = '''Update Books Set Copies = %d where BookID=%d''' % (
            book_count-1, bookid)
        sql.perform_db_actions(db_name, q2)

        print("Successfully issued the book")

def return_book(db_name):
    check_outbooks(db_name)
    given_id = input("Above are the list of transactions for borrowed book. "
                     "Enter the transaction id alone or Membership ID,Book ID: ")
    val1 = 0
    tid = -1
    bookid = -1
    try:
        if ',' in given_id:
            print("Membership ID and Books ID entered")
            val1 = given_id.split(",")
            val1[0] = int(val1[0])
            val1[1] = int(val1[1])
            val1 = tuple(val1)

            q1 = '''Select tid from Transactions where memid=%d and bookid= %d 
            and return_date is null ''' % (val1[0], val1[1])
            rows = perform_db_actions(db_name, q1)

            if len(rows) >= 1:
                tid = rows[0][0]
                bookid = val1[1]
            else:
                print("Error: Could not find the given transaction!")

        else:
            print("Transaction ID entered")
            val1 = int(given_id)
            q1 = "Select tid, bookid from Transactions where return_date is null and tid=%d" % (
                val1)
            rows = perform_db_actions(db_name, q1)
            if len(rows) >= 1:
                tid = val1
                bookid = rows[0][1]
            else:
                print("Error: Could not find the given transaction!")
    except Exception:
        print("Error: Data not found/Error Occurred! Please try again...")
    else:
        print("updating the database...")
        # increase copies count
        q1 = "Select Copies from Books where bookid=%d" % (bookid)
        rows = perform_db_actions(db_name, q1)
        q1 = "Update Books Set Copies =%d where Bookid=%d" % (
            rows[0][0]+1, bookid)
        perform_db_actions(db_name, q1)

        # update transaction
        q1 = '''Update Transactions Set return_date = '%s' 
        where tid =%d''' % (str(dt.datetime.now().strftime('%Y-%m-%d')), tid)
        rows = perform_db_actions(
            db_name, q1)
        print("All records updated!")