import sqlite3, sys
from getpass import getpass
from datetime import date
import random

def main():
    
    # establish connection with database
    global conn
    conn = sqlite3.connect(sys.argv[1])
    conn.row_factory = sqlite3.Row 

    # this global variable can be used on all function call inside main()
    global c
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON;')

    # THIS IS TO ERASE AND CREATE A DB!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    createDataBase() 

    # boot up welcome screen (which will give the login options)
    welcomeScreen()

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
    print("""===============================================================
    LOGIN SCREEN
===============================================================""")
    while True:
        # get the username via user input
        uid = input("Enter username: ").lower()

        # get the password via user inout
        pwd = getpass("Enter password: ")

        # store user if any
        global user
        user = retrieveUser(uid, pwd)

        # if a user exists break from loop
        if(user != None):
            print("""\n===============================================================
    Welcome {}! User#{}
===============================================================\n""".format(user[1], user[0]))
            sysFunc()
            break
        
        # else print login error
        else:
            choice = input("\nUsername or password is incorrect. Try Again? (yes/no):").lower()
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
    print("""===============================================================
    REGISTER SCREEN
===============================================================""")
    while True:
        # get the uid
        uid = input("Enter uid: ")

        while isUniqueUser(uid) != True:
            print("This uid is already taken. Please enter a different uid.")
            uid = input("Enter uid: ")

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
            print("""\n===============================================================
    Welcome {}! User#{}
===============================================================\n""".format(user[1], user[0]))
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
    print("""===============================================================
    SYSTEM FUNCTIONALITIES
===============================================================""")
    while True:
        print("""System functions:
        1 - Post a question
        2 - Search for posts
        """)
        func = input("Select function or type 'logout' or 'exit: ")

        # selecting system functions to run
        if str(func) == "1":
            postQuestion()
            break
        elif str(func) == "2":
            #call searchPost()
            end = False
            while end == False:
                our_Post= keyword_search()
                if (our_Post == None):
                    end = False
                else:
                    end = True
            post_action(our_Post)
            
            
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
postQuestion() - The Post Question Screen

Purpose: This is the interface where users can post a question
-----------------------------------------------------------------'''
def postQuestion():
    print("""===============================================================
    POST A QUESTION
===============================================================""")

    # get data
    title = input("Enter Title of Question: ")
    body = input("Enter Body of Question: ")

    # generate a pid
    pid = random.randint(1000, 9999)

    # check if pid is unqiue
    # while not unique generate a random pid
    while isUniquePost(pid) != True:
        pid = random.randint(1000, 9999)

    # pdate is date today
    pdate = date.today()

    # try to insert to db
    c.execute("""
        insert into posts
        values (:pid, :pdate, :title, :body, :poster)
        """, {"pid":pid, "pdate":pdate, "title":title, "body":body, "poster": user[0]})

    # insert newly created question to question table
    c.execute("""
        insert into questions
        values(:pid, :theaid)
    """, {"pid":pid, "theaid": None})

    print("""\n===============================================================
    Question Post#{} successfully posted!
===============================================================\n""".format(pid))
    
    sysFunc() # go back to system functions menu

""" -------------------------------
Purpose: Asks the user to enter one or more keywords.

Input: None
Output: returns the list of keywords
-------------------------------------"""
def ask_for_keywords():
	keyword_list = [] # List of keywords that the user has entered
	search_keyword = True # The user is still searching keywords

	while search_keyword: 
		user_keyword = input('\nEnter one or more keywords to narrow down your search: ')
		while len(user_keyword.strip()) == 0: # Assuming that the user has entered an empty string
			user_keyword = input('\nEnter one or more keywords to narrow down your search: ')

		user_input = '%' + user_keyword.strip() + '%'
		if user_input.lower() in keyword_list: # If the user enters the same keyword (since LIKE is case-insensitive)
			print('\nYou have already entered that keyword.')
		else:
			keyword_list.append(user_input) # Adds the keyword to the list

		continue_search = input('\nWould you like to enter another keyword? (y/n)?: ').lower()

		while continue_search not in ('y','n'): # If the user does not enter yes or no
			continue_search = input('\nPlease enter a valid input (y/n): ').lower()

		if continue_search == 'n': # If the user no longer wants to enter any more keywords
			search_keyword = False # The user is done searching

	return keyword_list 

""" -------------------------------
Purpose: Groups the keyword count for posts with the same postID, but different keyword(s) together
eg. post1 contains keyword1 and keyword2, giving it a total of 2.

Input: None
Output: returns the list of keywords
-------------------------------------"""
def group_keyword_count(order_track):

	temp_dict = {} # Temporary dictionary

	for tup in order_track: # Iterates over the tuples 
		temp_dict[tup[0]] = 0 # Each postID wil act as a key and will start off with a keyword count of 0 intiially

	for key in temp_dict.keys(): 
		for tup in order_track:
			if tup[0] == key: # Checks if each postID occurs more than once, and if it does, adds the keyword counts together
				temp_dict[tup[0]] += tup[1]

	order_track = list(tuple(temp_dict.items())) # Order track will become a list of tuples again
	order_track.sort(key =lambda order_list: order_list[1], reverse = True) # Will be sorted based on keyword count
	return order_track 

""" -------------------------------------------------
Purpose: The posts that contains the keywords will be displayed.

Input: None
Output: returns the postID that the user has selected
-----------------------------------------------------"""
def keyword_search(): 

	keyword_list = ask_for_keywords()

	order_track = [] # A list that will be used later to keep track of the posts and the order that they should be displayed in

	# Keeps track of all the posts to prevent them from being displayed again (eg. if two keywords are in the same post)
	post_list = [] 

	for keyword in keyword_list: 

		c.execute("""SELECT p_count.pid, COUNT(p_count.pid) AS pcount
				 
					FROM (SELECT posts.pid from posts where title LIKE ?

					UNION 

					SELECT posts.pid from posts where body LIKE ?

					UNION 
	
					SELECT tags.pid from tags, posts 

					where tags.pid = posts.pid AND tag LIKE ?) p_count
					
					GROUP BY p_count.pid
					
					ORDER BY pcount DESC

					;""", (keyword, keyword, keyword,)) 

		# ----------------------------------------------
		# The following is used to determine the order that the posts will be displayed in (based the number of keywords
		# that show up in each result)
		row = c.fetchall()
		for each in row:
			order_track.append((each['pid'],each['pcount']))  
			# Used to keep track of the postID and the keyword count (known as pcount)
			# eg. [(pid: 001, pcount: 2), (pid: 002, pcount: 3)]

		order_track.sort(key =lambda order_list: order_list[1], reverse = True)
		# Sorts the list based on the keyword count, or the second element of each tuple (in descending order)
		# eg. Taken from the example above, [(pid: 001, pcount: 3), (pid: 002, pcount: 2)]
		# -------------------------------------------------

	select_options = {} 
	# Will be used to keep track of the post that the user has selected.
	# eg. {'1': p005, '2': p006}
	# If the user enters '1' as their input later on, then 'p005' will be returned

	# The max variable will  store how many posts will be displayed at one time 
	# (eg. 5 posts will be displayed for the first time, and 10 posts will
	# be displayed for the second time).
	max = 0 

	selected = False # The user has not selected a post yet
	reached_max = False # The max number of posts has not been displayed

	# ----------------------------------------------------------------------
	order_track = group_keyword_count(order_track)
	# ---------------------------------------------------------------------

	while not selected:
		max += 5 # Determines how many posts will be displayed
		for num in range(max):
			try:
				current = order_track[num][0] # Order track in the form of eg. [('p001', 5), ('p008', 2)]

				# For each post from the ordered list (order_track), its information will be displayed.
				c.execute("""SELECT p.pid, p.title, p.body, p.pdate, p.poster, 

					IFNULL(v_count.vcount,0) AS vcount, IFNULL(a_count.acount,0) AS acount, q.qpid
				 
					FROM posts p
					
					LEFT OUTER JOIN (SELECT v.pid, COUNT(v.vno) as vcount FROM votes v GROUP BY v.pid) v_count
				
					ON p.pid = v_count.pid LEFT OUTER JOIN (SELECT a.qid, COUNT(a.pid) AS acount 
					
					FROM answers a GROUP BY a.qid) a_count ON p.pid = a_count.qid LEFT OUTER JOIN (SELECT q.pid AS qpid FROM 
					
					questions q) q ON p.pid = q.qpid

					WHERE p.pid = ?""", (current,))


			except IndexError: 
				reached_max = True
				 # Posts will be displayed in multiples of 5. Ignore error if it is not a multiple of 5 (eg. 13 posts)

			except UnboundLocalError: # Assuming that the user does not enter a valid keyword (eg. '   ')
				continue
	   
			display = c.fetchall()
	
			# -------------------------------------------------------------------------------
			for each in display:
				if each['pid'] not in post_list: # If the post has not been displayed yet (in case of multiples of the same post)
					print('---------------------------------------------------')
					post_list.append(each['pid']) # Keeps track of posts that have already been posted
			
					print('Result ' + str(num+1) + '\n\n' + 'postID: ' + each['pid'] + '\n' + 
						'Type of post: ' + ('Question' if each['qpid'] != None else 'Answer') + '\n'
						'Title: ' + each['title'] + '\n' + 
						'Date: ' + str(each['pdate']) + '\n' + 'Poster: ' + each['poster'] + '\n' +
						'Number of votes: '+ str(each['vcount']) + '\n' + 
						'Number of answers: ' + str('N/A' if each['acount'] == 0 and each['qpid'] == None
						else each['acount']) + '\n' + 'Body: ' +  
                        (each['body'] if (len(each['body']) < 30) else (each['body'] + '...')))
						# If the post is an answer, then the number of answers is N/A.

					select_options[str(num+1)] = each['pid'] # Adds the post option into the list of possible options for user
			# ----------------------------------------------------------------------------------------------------------------
		if len(post_list) == 0: # If no posts are displayed
			print('\nNo posts are displayed. Please try using other valid keywords.')
			return 

		if not reached_max: # If more posts can be displayed			
			user_select = input("\nSelect a post displayed above, or type in 's' to see more posts. \n")
		else:
			user_select = input("\nSelect a post displayed above:  \n")

		# ---------------------------------------------------------------------------------------------------------
		if user_select in select_options.keys(): # If the user selects a post result number that is displayed above
			return select_options[user_select]
		elif user_select == 's':
			continue
		else:
			valid_input = False # The user did not enter a valid input
			while not valid_input:
				user_select = input('Please enter a valid input: ')
				if user_select in select_options.keys(): # If the user selects a post result number that is displayed above
					return select_options[user_select]
				elif user_select == 's': 
					break
		# ----------------------------------------------------------------------------------------------------------
		
""" ------------------------------------------------------------
Purpose: If the post is an answer, a privileged user can mark
an answer as the accepted answer, or leave it as it is.
Input: postID that belongs to an answer
Output: None
--------------------------------------------------------------"""

def mark_accepted(post_id):
	
    check = c.execute("SELECT uid FROM privileged WHERE uid =:user_id;", ({'user_id': user}))
   
    if c.fetchone() == None:
        print("You are not a privledged user, so you cannot perform this action.\n")
        return
	
    row = c.execute("SELECT pid FROM questions")
    for each in row:
        if each['pid'] == post_id: # If the post that the user has selected is a question
	        print("\nThe post you have selected is a question. Therefore, this option is not valid.")
	        return

    # Finding the question ID and the current accepted answer (the current postID is the input)
    c.execute("SELECT a.qid, q.theaid FROM answers a, questions q WHERE a.qid = q.pid AND a.pid = ?", (post_id,))
    
    row = c.fetchone() # Only one output is to be expected
    
    if row['theaid'] != None: # If an accepted answer exists
        acc_answer = row['theaid']  # The postID of the accepted answer
            
        # Gets input from the user if they would like to change the accepted answer
        print("An accepted answer already exists.\n")
        a_exists = input("Would you like to change the accepted answer? \n 1. Yes \n 2. No \n")
        while a_exists not in ('1','2'):
            a_exists = input("Please enter a valid input: ")


    else: # If an accepted answer does not exist
        a_exists = input("Would you like to mark this as the accepted answer? \n 1. Yes \n 2. No \n")
        while a_exists not in ('1','2'):
            a_exists = input("Please enter a valid input: ")



    if a_exists == '1': # If the user wants to change the accepted answer

            # --------------------------------------------------------------------------------
            # If the user is changing the accepted answer to the current accepted answer
            if row['theaid'] == post_id:
                    print("This post is already the accepted answer of the question.")
            # --------------------------------------------------------------------------------

            else: # Changes the current accepted answer to the answer that the user has chosen
                c.execute("""UPDATE questions SET theaid = ? WHERE pid = 
                         (SELECT a.qid FROM answers a WHERE a.pid = ?)""", (post_id, post_id))


    conn.commit()
    return

""" -----------------------
Purpose: Allows the privileged user to give the poster a badge. 
Input: postID
Output: None
---------------------------"""
def give_badge(post_id):
	
    	check = c.execute("SELECT uid FROM privileged WHERE uid =:user_id;", ({'user_id': user}))
   
    	if c.fetchone() == None:
            print("You are not a privledged user, so you cannot perform this action.\n")
            return

	current = date.today() # The current date 

	c.execute('SELECT poster FROM posts WHERE pid = ?;', (post_id,))
	row = c.fetchone() # Only one output is expected
	poster_id = row['poster'] # Finds the poster of the selected post
	
	c.execute('SELECT rowid, bname FROM badges ORDER BY rowid; ') # rowIDs are used to give numbered options to the user
	row = c.fetchall()

	possible_options = [] # Keeps track of all the possible numbered options the user can choose from
	for b_info in row:
		possible_options.append(str(b_info['rowid']))
		print(b_info['rowid'],b_info['bname']) # Displaying the badge options for the user to choose from

	# User enters a number that corresponds to the badge name
	b_name_input = input('\nWhich badge would you like to give? Enter the number that is associated with the badge: ')
	while b_name_input not in possible_options:
		b_name_input = input('\nPlease enter a valid number that is associated with a badge: ')


	for each in row:
		if str(each['rowid']) == b_name_input:
			b_name_input = each['bname'] # Finds the badge name based on the number given by the user

	# Stores the poster, the current date, and the badge selected
	b_add = {'uid': poster_id, 'bdate': current, 'b_name': b_name_input}
	
	try:
	    c.execute('INSERT INTO ubadges VALUES (:uid, :bdate,:b_name)', b_add)
	except sqlite3.Error as e:
	    print("\nYou cannot give a badge to the same user on the same day.")
	    return

	c.execute('INSERT INTO ubadges VALUES (:uid, :bdate,:b_name)', b_add)
	print('\nBadge has been given!')

	conn.commit()

	return
""" -------------------------------------------------
Purpose: Allows a user to add a vote on the 
post(for which its post id is passed as input)

Input: post_id: the pid of the post
Output: None
-----------------------------------------------------"""
def vote(post_id):
    #get the current user's uid
    global user
    user_id = user[0]
    current = date.today()
    #this makes sure the post exists
    c.execute("SELECT * FROM posts p1 WHERE p1.pid=:ourPid",{"ourPid":post_id} )
    rows = c.fetchall()
    if len(rows) < 1:
        print("This post does not exist. Vote rejected")
        #conn.commit()
        #conn.close()
        return
    #this makes sure the user has not already voted on this specific post
    c.execute("SELECT pid FROM votes WHERE pid =:ourPid AND uid=:ourUser",{"ourPid":post_id, "ourUser":user_id} )
    rows = c.fetchall()
    if len(rows) > 0:
        print("You have already voted on this post. Vote rejected")
        #conn.commit()
        #conn.close()
        return
    #this is used to get a new distinct vno by getting all previous vno's and making our new vno 1+(max of all previous vno)
    c.execute("SELECT DISTINCT vno FROM votes")
    rows = c.fetchall()
    max = 0
    num = len(rows)
    for i in range(0, num):
        if rows[i][0] > max:
            max = rows[i][0]
    newVn = max +1
    #conn.commit()
    #add our new vote to the database
    c.execute("INSERT INTO votes VALUES (:ourPid, :ourVn, :ourVoteDate, :ourUser);", {'ourPid': post_id, 'ourVn': newVn, 'ourVoteDate': current, 'ourUser': user_id})
    print("Vote added!")
    conn.commit()

""" -------------------------------------------------
Purpose: Allows a privileged user to add a tag on the 
post(for which its post id is passed as input)
the user is given a choice of what the tag should say
and gets a chance to enter this via the command line

Input: post_id: the pid of the post
Output: None
-----------------------------------------------------"""
def tag(post_id):
    #get the current user's uid
    global user
    user_id = user[0]

    #this makes sure the user is privileged
    c.execute("SELECT * FROM privileged WHERE uid =:ourUser",{"ourUser":user_id} )
    rows = c.fetchall()
    if len(rows) < 1:
        print("You are not a priviledged user and thus cannot add tags to posts. Tag rejected")
        #conn.commit()
        #conn.close()
        return


    #this makes sure the post exists
    c.execute("SELECT * FROM posts p1 WHERE p1.pid=:ourPid",{"ourPid":post_id} )
    rows = c.fetchall()
    if len(rows) < 1:
        print("This post does not exist. Tag rejected")
        #conn.commit()
        #conn.close()
        return

    #get the user's input for the tag's content
    tag = input("What would you like the tag to say? Enter 'exit' to exit or 'logout' to logout: ") 
    #test to see if the user is trying to exit or loggout and proceed accordingly
    if tag.lower() == 'exit':
        exit()
    if tag.lower() == 'logout':
        logout()

    #this is for making sure another tag does not exist where the pid is the same and tag is the same (here case ie lowercase or uppercase should
    #not factor in .lower() is used to assure this) knowledge of lower function from https://www.programiz.com/python-programming/methods/string/lower
    c.execute("SELECT pid, tag FROM tags")
    rows = c.fetchall()
    num = len(rows)

    for i in range(0, num):
        if rows[i][0].lower() == post_id.lower():
            if rows[i][1].lower() == tag.lower():
                print("This post already has this tag. Tag rejected")
                conn.commit()
                return

    #add the tag to the batabase
    c.execute("INSERT INTO tags(pid,tag) VALUES (:ourPid, :ourTag);", {'ourPid': post_id, 'ourTag': tag})
    print("Tag added")
    
    conn.commit()
    return


""" -------------------------------------------------
Purpose: Allows a privileged user to edit a
post(for which its post id is passed as input)
the user is given a choice as to wether they want to 
edit the title and/or the body of the post
and gets a chance to enter their choices via the command line
Depending on their choices the user can then enter in
the new titles and/or body once again via the command line

Input: post_id: the pid of the post
Output: None
-----------------------------------------------------"""
def edit(post_id):
    #get the current user's uid
    global user
    user_id = user[0]

    #this makes sure the user is privileged exists
    c.execute("SELECT * FROM privileged WHERE uid =:ourUser",{"ourUser":user_id} )
    rows = c.fetchall()
    if len(rows) < 1:
        print("You are not a priviledged user and thus cannot add tags to posts. Edit rejected")
        conn.commit()
        #conn.close()
        return

    #this makes sure the post exists
    c.execute("SELECT * FROM posts p1 WHERE p1.pid=:ourPid",{"ourPid":post_id} )
    rows = c.fetchall()
    if len(rows) < 1:
        print("This post does not exist. Edit rejected")
        conn.commit()
        #conn.close()
        return

    #get the user's choice for wether or not they would like the edit the post's title
    updateTitleChoice = input("Would you like to edit the Title? Enter 'yes' or 'no' or 'exit' to exit or 'logout' to logout: ")
    updateTitleChoice = updateTitleChoice.lower()
    
    #this continues to loop untill a valid choice is made
    while (True):
        if updateTitleChoice == "yes":
            #user wants to edit the title
            updateTitle = True
            #if the user chooses exit or logout proceed accordingly else this is the new title
            newTitle = input("What would you like the new Title to be? Enter 'exit' to exit or 'logout' to logout: ")
            if newTitle.lower() == 'exit':
                exit()
                return
            elif newTitle.lower() == 'logout':
                logout()
                return
            else:
                break
        elif updateTitleChoice == "no":
            #user does not want to edit the title
            updateTitle = False
            break
        elif updateTitleChoice == "exit":
            #user wants to exit
            exit()
            return
        elif updateTitleChoice == "logout":
            #user wants to logout
            logout()
            return
        else:
            #user's choice was not a valid one. Ask them for a new choice
            updateTitleChoice = input("Invalid choice please choose a valid action from either 'yes','no,'exit' or 'logout': ")
            updateTitleChoice = updateTitleChoice.lower()

    #get the user's choice for wether or not they would like the edit the post's body
    updateBodyChoice = input("Would you like to edit the Body? Enter 'yes' or 'no' or 'exit' to exit or 'logout' to logout: ")
    updateBodyChoice = updateBodyChoice.lower()

    #this continues to loop untill a valid choice is made
    while (True):
        if updateBodyChoice == "yes":
            #user wants to edit the Body
            updateBody = True
            #if the user chooses exit or logout proceed accordingly else this is the new body
            newBody = input("What would you like the new Body to be? Enter 'exit' to exit or 'logout' to logout: ")
            if newBody.lower() == 'exit':
                exit()
                return
            elif newBody.lower() == 'logout':
                logout()
                return
            else:
                break
        elif updateBodyChoice == "no":
            #user does not want to edit the body
            updateBody = False
            break
        elif updateBodyChoice == "exit":
            #user wants to exit
            exit()
            return
        elif updateBodyChoice == "logout":
            #user wants to logout
            logout()
            return
        else:
            #user's choice was not a valid one. Ask them for a new choice
            updateBodyChoice = input("Incorrect choice please choose a valid action from either 'yes','no,'exit' or 'logout': ")
            updateBodyChoice = updateBodyChoice.lower()
            


    if updateTitle == True:
        if updateBody == True:
            #the user chose yes to update title and update body, update these fields in the database accoding to the new values supplied
            #update format found on https://www.w3schools.com/sql/sql_update.asp
            c.execute("UPDATE posts SET title = :ourTitle, body = :ourBody WHERE pid = :ourPid;",{"ourTitle":newTitle,"ourBody":newBody, "ourPid":post_id})
            print("Body and Title updated. Edit accepted")
        
        else:
            #the user chose yes to update title and no to update body, update this field in the database accoding to the new value supplied
            c.execute("UPDATE posts SET title = :ourTitle WHERE pid = :ourPid;",{"ourTitle":newTitle, "ourPid":post_id})
            print("Title updated. Edit accepted")
    else:
        if updateBody == True:
            #the user chose no to update title and yes to update body, update this field in the database accoding to the new value supplied
            c.execute("UPDATE posts SET body = :ourBody WHERE pid = :ourPid;",{"ourBody":newBody, "ourPid":post_id})
            print("Body updated. Edit accepted")
        else:
            #the user chose no to update title and no to update body, no update to the database but user is told they were able to perform an edit
            # ie they are a privileged user and the post exists
            print("No updates performed. Edit accepted")
    
    
    conn.commit()
    return

""" -------------------------------------------------
Purpose: Displays the Screen which contains all the post
actions availible to the user. Then prompts the user to
enter their choice of action and takes the corrent action
accordinglt

Input: post_id: the pid of the current selected post
Output: None
-----------------------------------------------------"""
def post_action(pid):
    #dispay all the post actions availible to the user (including of course exit and logout)
    print("""==================================================\n    POST ACTIONS\n==================================================""")
    print("What action would you like to perform on this post?")
    print("Enter 1 to post an answer for this post")
    print("Enter 2 to vote on this post")
    print("Enter 3 to mark the post as accepted")
    print("Enter 4 to give a badge to the poster of this post")
    print("Enter 5 to add a tag to the post")
    print("Enter 6 to edit the title and/or body of the post")
    print("Enter 'back' to go back to system functionalities page")
    print("Or enter 'exit' to exit or 'logout' to logout")
    #gets the users choice of post action
    action = input("What action would you like to take? ") 
    action = action.lower()
    #loops untill a valid choice is made
    while (True):
        #user chose to post ananswer to this post
        if action.lower() == '1':
            # assert that pid is a question post
            if isQuestion(pid) == True:
                # call postAnswer()
                postAnswer(pid)
                break
            else: #selected post is not a question
                print("\nYou have not selected a question post\n")
                break
        elif action.lower() == '2':
            #user chose to place a vote on this post
            vote(pid)
            break
        elif action == '3':
            #user chose to mark this post as accepted
            mark_accepted(pid)
            break
        elif action == '4':
            #user chose to give a badge to the poster of this post
            give_badge(pid)
            break
        elif action == '5':
            #user chose to add a tag to the post
            tag(pid)
            break
        elif action == '6':
            #user chose to edit the title and/or body of the post
            edit(pid)
            break
        elif action == 'back':
            #user wishes to return to system functionalities page
            sysFunc()
            break
        elif action == 'exit':
            #user wishes to exit
            exit()
            return
        elif action == 'logout':
            #user wishes to logout
            logout()
            return
        else:
            #users did not make a valid choice, get a new choice
            action = input("Invalid action please choose a valid action from either '1','2','3','4','5','6','back,'exit' or 'logout': ")
            action = action.lower()
    #after the post action is completed ask the user if they would like to perform another post action on this post
    print("What would you like to perform another action on this post? ")
    response = input("Enter 'yes' or 'no' or 'exit' to exit or 'logout' to logout: ")
    response = response.lower()
    #loop untill the user choses a valid option
    while (True):
        if response == 'no':
            #user does not wish to perform another post-action, go back to system functionalities page
            sysFunc()
        elif response == 'yes':
            #user does wish to perform another post-action, make a recursive call to restart this function
            post_action(pid)
        elif response == 'exit':
            #user wishes to exit
            exit()
            return
        elif response == 'logout':
            #user wishes to logout
            logout()
            return
        else:
            #user did not supply a valid choice. Prompt the user for another choice
            response = input("Invalid input please enter 'yes, 'no', 'exit' or logout': ")
            response = response.lower()
    return

'''-----------------------------------------------------------------
postAnswer() - The Post Answer Screen

Purpose: This will allow the user to post an answer to selected post

Params: qid - the question post this is answering
-----------------------------------------------------------------'''
def postAnswer(qid):
    question = retrievePost(qid)
    print("""\n==================================================
    POST AN ANSWER to Post#{}
    "{}"
==================================================\n""".format(qid, question[2]))

    # get data
    title = input("Enter Title of Answer: ")
    body = input("Enter Body of Answer: ")

    # generate a pid
    pid = random.randint(1000, 9999)

    # check if pid is unqiue
    # while not unique generate a random pid
    while isUniquePost(pid) != True:
        pid = random.randint(1000, 9999)
    
    # pdate is date today
    pdate = date.today()

    # try to insert to db
    c.execute("""
        insert into posts
        values (:pid, :pdate, :title, :body, :poster)
        """, {"pid":pid, "pdate":pdate, "title":title, "body":body, "poster": user[0]})
    
    print("""=============================================================================
    Answer successfully posted! 
    Question #{}: "{}"
    Answer #{}: "{}"
=============================================================================""".format(qid, question[2], pid, title))

'''-----------------------------------------------------------------
isUniqueUser() - Helper function: Check if unique user id

Purpose: Given a uid check if it is unique

Params: uid - the id of the user

Return: a boolean
-----------------------------------------------------------------'''
def isUniqueUser(uid):
    c.execute("""
        select *
        from users u
        where u.uid = :uid
    """, {"uid": uid})

    result = c.fetchone()

    if result == None:
        return True
    else:
        return False

'''-----------------------------------------------------------------
isUniquePost() - Helper function: Check if unique post id

Purpose: Given a pid check if it is unique

Params: pid - the id of the post

Return: a boolean
-----------------------------------------------------------------'''
def isUniquePost(pid):
    c.execute("""
        select *
        from posts p
        where p.pid = :pid
    """, {"pid": pid})

    result = c.fetchone()

    if result == None:
        return True
    else:
        return False

'''-----------------------------------------------------------------
isQuestion() - Helper function: Check if this is a question post

Purpose: This function will check if a pid is a question. return true
if yes, else false

Params: pid - the unique id of the post

Return: a boolean
-----------------------------------------------------------------'''
def isQuestion(pid):
    c.execute("""
        select *
        from questions q
        where q.pid = :pid
    """, {"pid": pid})

    result = c.fetchone()

    # if pid is found in questions table
    if result != None:
        return True
    else:
        return False
'''-----------------------------------------------------------------
retrievePost() - Helper function: Retrieve post data from db

Purpose: This function will retrieve and return a post from db
given pid

Params: pid - the unique id of the post

Return: a tuple of post data or None
-----------------------------------------------------------------'''
def retrievePost(pid):
    c.execute("""
        select *
        from posts p
        where p.pid = :pid
    """, {"pid": pid})
    
    return c.fetchone()

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
    """, {"uid":uid.lower(), "pwd":pwd})

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
    # this will print when exit() is called, exit() will return here
    print("\nGoodbye!\n")

    # standard
    conn.commit()
    conn.close()
    sys.exit()

def drop_tables():
    global conn, c

    drop_answers = "DROP TABLE IF EXISTS answers";
    drop_questions = "DROP TABLE IF EXISTS questions";
    drop_votes = "DROP TABLE IF EXISTS votes";
    drop_tags = "DROP TABLE IF EXISTS tags";
    drop_posts = "DROP TABLE IF EXISTS posts";
    drop_ubadges = "DROP TABLE IF EXISTS ubadges";
    drop_badges = "DROP TABLE IF EXISTS badges";
    drop_users = "DROP TABLE IF EXISTS users";
    drop_privileged = "DROP TABLE IF EXISTS privileged";

    c.execute(drop_answers)
    c.execute(drop_questions)
    c.execute(drop_votes)
    c.execute(drop_tags)
    c.execute(drop_posts)
    c.execute(drop_ubadges)
    c.execute(drop_badges)
    c.execute(drop_privileged)
    c.execute(drop_users)
    


def define_tables():
    global conn, c

    users_query = '''
    create table users (
    uid		char(4),
    name		text,
    pwd       text,
    city		text,
    crdate	date,
    primary key (uid)
    );
    '''

    badges_query = '''
    create table badges (
    bname		text,
    type		text,
    primary key (bname)
    );
    '''

    ubadges_query = '''
    create table ubadges (
    uid		char(4),
    bdate		date,
    bname		text,
    primary key (uid,bdate),
    foreign key (uid) references users,
    foreign key (bname) references badges
    );
    '''

    posts_query = '''
    create table posts (
    pid		char(4),
    pdate		date,
    title		text,
    body		text,
    poster	char(4),
    primary key (pid),
    foreign key (poster) references users
    );
    '''

    tags_query = '''
    create table tags (
    pid		char(4),
    tag		text,
    primary key (pid,tag),
    foreign key (pid) references posts
    );
    '''

    votes_query = '''
    create table votes (
    pid		char(4),
    vno		int,
    vdate		text,
    uid		char(4),
    primary key (pid,vno),
    foreign key (pid) references posts,
    foreign key (uid) references users
    );
    '''

    questions_query = '''
    create table questions (
    pid		char(4),
    theaid	char(4),
    primary key (pid),
    foreign key (theaid) references answers
    );
    '''

    answers_query = '''
    create table answers (
    pid		char(4),
    qid		char(4),
    primary key (pid),
    foreign key (qid) references questions
    );
    '''

    privileged_query = '''
    create table privileged (
    uid		char(4),
    primary key (uid),
    foreign key (uid) references users
    );
    '''

    c.execute(users_query)
    c.execute(badges_query)
    c.execute(ubadges_query)
    c.execute(posts_query)
    c.execute(tags_query)
    c.execute(votes_query)
    c.execute(questions_query)
    c.execute(answers_query)
    c.execute(privileged_query)

    return


def insert_data():

    c.execute('''insert into users(uid,name,pwd,city,crdate) VALUES ('u001','Vince Wain', 123, 'Edmonton', 2019-01-05);''')
    c.execute('''insert into posts(pid,pdate,title,body,poster) VALUES ('p001',2019-01-06, 'What can I do to earn badges?', 'What kind of posts do people tend to give out badges for?','u001');''')
    c.execute('''insert into tags(pid,tag) VALUES ('p001','richardisbesT');''')
    c.execute('''insert into privileged(uid) VALUES ('u001');''')
    conn.commit()
    return

def createDataBase():
    drop_tables()
    define_tables()
    insert_data()

main()
