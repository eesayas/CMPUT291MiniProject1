import sqlite3
from getpass import getpass
from datetime import date

def main():
    # establish connection with database
    conn = sqlite3.connect("data.db")

    # this global variable can be used on all function call inside main()
    global c
    c = conn.cursor()

    # boot up welcome screen (which will give the login options)
    welcomeScreen()

    # this will print when exit() is called, exit() will return here
    print("\nGoodbye!\n")

    # standard
    conn.commit()
    conn.close()

'''-----------------------------------------------------------------
welcomeScreen() - The Welcome Screen

Purpose: This will give the user options to login. If user is 
registered loginScreen() will be called else registerScreen() will
be called.
-----------------------------------------------------------------'''
def welcomeScreen():
    print("\nWelcome to CMPUT 291 Mini Project 1!\n")
    while True:
        print("""Login Options:
        1 - I am Registered
        2 - I am Unregistered""")

        # get login option of user
        option = input("Select option or type 'exit' to terminate: ")
        
        # selecting login functions to run
        if str(option) == "1":
            user = loginScreen()
            break
        elif str(option) == "2":
            registerScreen()
            break
        elif str(option).lower() == "exit":
            exit()
            break
        else:
            print("\nYou've enter an invalid option\n")

'''-----------------------------------------------------------------
loginScreen() - The Login Screen

Purpose: This will get the uid, pwd from user input and will search
the database for any matches. If match found, continue to System
Functionalities sysfunc(). Else, print a login error message and show 
interface again.
-----------------------------------------------------------------'''
def loginScreen():
    print("""==================================================
    LOGIN SCREEN
==================================================""")
    while True:
        # get the username via user input
        uid = input("Enter username: ")

        # get the password via user inout
        pwd = getpass("Enter password: ")

        # store user if any
        global user
        user = retrieveUser(uid, pwd)

        # if a user exists break from loop
        if(user != None):
            sysFunc()
            break
        
        # else print login error
        else:
            choice = input("\nUsername or password is incorrect. Try Again? (yes/no):")
            if(str(choice) != "yes"):
                welcomeScreen()
                break
            
'''-------------------------------------------------------------------------
registerScreen() - The Register Screen

Purpose: This will ask the user to provide a unique id, a name, a city and 
a password. Use this data to create a new user to insert to the database.
Data will also have crdate, which is the current date. When register is
successful move on to system functionalities sysfunc().
-------------------------------------------------------------------------'''
def registerScreen():
    print("""==================================================
    REGISTER SCREEN
==================================================""")
    while True:
        # get the uid
        uid = input("Enter uid: ")
        # check if unique

        # get data
        name = input("Enter name: ")
        city = input("Enter city: ")
        pwd = input("Enter password: ")
        crdate = date.today()

        # try to insert to db
        c.execute("""
        insert into users
        values (:uid, :name, :pwd, :city, :crdate)
        """, {"uid":uid, "name":name, "pwd":pwd, "city":city, "crdate":crdate})
   
        # store user if any
        global user
        user = retrieveUser(uid, pwd)

        # if a user exists break from loop
        if(user != None):
            sysFunc()
            break
        
        # else print login error
        else:
            choice = input("\nThere was an error in registering. Try Again? (yes/no):")
            if(str(choice) != "yes"):
                welcomeScreen()
                break
            
'''-----------------------------------------------------------------
sysFunc() - The System Functionalities

Purpose: This is the interface where users can either post a question
or search for a post to do further post actions
-----------------------------------------------------------------'''
def sysFunc():
    print("""==================================================
    SYSTEM FUNCTIONALITIES
==================================================""")
    while True:
        print("""System functions:
        1 - Post a question
        2 - Search for posts
        """)
        func = input("Select function or type 'logout' or 'exit: ")

        # selecting system functions to run
        if str(func) == "1":
            #call postQuestion()
            break
        elif str(func) == "2":
            #call searchPost()
            break
        elif str(func).lower() == "logout":
            logout()
            break
        elif str(func).lower() == "exit":
            exit()
            break
        else:
            print("\nYou've enter an invalid function\n")

'''-----------------------------------------------------------------
retrieveUser() - Helper function: Retrieve user data from db

Purpose: This function will retrieve and return a user from db
given uid and pwd

Params: uid - the unique id of the user
        pwd - the password of the user

Return: a tuple of user data or None
-----------------------------------------------------------------'''
def retrieveUser(uid, pwd):
    # try to get credentials from db
    c.execute("""
    select *
    from users u
    where u.uid = :uid and u.pwd = :pwd
    limit 1; 
    """, {"uid":uid, "pwd":pwd})

    return c.fetchone()

'''-----------------------------------------------------------------
logout() - Helper function: Logout

Purpose: This function will clear the user variable and return
to Welcome Screen
-----------------------------------------------------------------'''
def logout():
    global user
    user = None
    welcomeScreen()

'''-----------------------------------------------------------------
exit() - Helper function: exit 

Purpose: This function will exit the program entirely and clear the
user variable
-----------------------------------------------------------------'''
def exit():
    global user
    user = None
    return

main()