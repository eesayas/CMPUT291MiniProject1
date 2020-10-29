import sqlite3
from getpass import getpass

def main():
    # establish connection with database
    conn = sqlite3.connect("data.db")

    # provide a Welcome screen interface
    print("\nWelcome to CMPUT 291 Mini Project 1!\n")
    print("""Login Options:
    1 - I am Registered
    2 - I am Unregistered
    
    Enter any other key to exit
    """)

    # get login option of user
    option = input("Select a login option: ")
    
    # selecting login functions to run
    if str(option) == "1":
        user = loginScreen(conn)
    elif str(option) == "2":
        registerScreen()
    else:
        print("\nGoodbye!\n")
        return

'''--------------------------------------------------------------'''

'''-----------------------------------------------------------------
loginScreen() - This will fire when user selects "1" in Login Options

Purpose: This will get the uid, pwd from user input and will search
the database for any matches. If match found, continue to System
Functionalities. Else, print a login error message and show interface
again.

Parameters: conn - connection to database
-----------------------------------------------------------------'''
def loginScreen(conn):
    while True:
        # get the username via user input
        uid = input("Enter username: ")

        # get the password via user inout
        pwd = getpass("Enter password: ")

        # try to get credentials from db
        c = conn.cursor()
        c.execute("""
        select *
        from users u
        where u.uid = :uid and u.pwd = :pwd
        limit 1; 
        """, {"uid":uid, "pwd":pwd})
   
        # store user if any
        user = c.fetchone()

        # if a user exists break from loop
        if(user != None):
            return user
        
        # else print login error
        else:
            print("Username or password is incorrect. Try Again.")

'''-------------------------------------------------------------------------
registerScreen() - This will fire when user selects "2" in Register Options

Purpose: This will ask the user to provide a unique id

Parameters: conn - connection to database
-------------------------------------------------------------------------'''
def registerScreen():
    print("hello")

main()