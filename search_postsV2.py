'''SPEC: Search for posts.The user should be able to provide one or more keywords, 
    and the system should retrieve all posts that contain at least one keyword either in title, body, or tag fields.
        
    For each matching post, in addition to the columns of posts table, the number of votes, and the number of 
    answers if the post is a question (or zero if the question has no answers) should be displayed. 

    The result should be ordered based on the number of matching keywords with posts matching the 
    largest number of keywords listed on top. If there are more than 5 matching posts, 
    at most 5 matches will be shown at a time, letting the user select a post or see more matches. 
    The user should be able to select a post and perform a post action (as discussed next).'''

import sqlite3, sys
from datetime import datetime

conn = sqlite3.connect(sys.argv[1]) # Pass the database as a command line argument
conn.row_factory = sqlite3.Row 
c = conn.cursor()
c.execute('PRAGMA foreign_keys = ON;')

""" -------------------------------
Asks the user to enter one or more keywords.

Input: None
Output: returns the list of keywords
-------------------------------------"""
def ask_for_keywords():
	keyword_list = []
	search_keyword = True # The user is still searching keywords

	while search_keyword: 
		user_input = '%' + input('\nEnter one or more keywords to narrow down your search: ') + '%'
		keyword_list.append(user_input) # Adds the keyword to the list
		continue_search = input('\nWould you like to enter another keyword? (y/n)?: ').lower()

		if continue_search == 'n': # If the user no longer wants to enter any more keywords
			search_keyword = False # The user is done searching

	return keyword_list

""" -------------------------------------------------
The posts that contains the keywords will be displayed.

Input: list of keywords
Output: returns the postID that the user has selected

-----------------------------------------------------"""

def keyword_search(): 
	
	keyword_list = ask_for_keywords()

	order_track = [] # A list that will be used later to keep track of the posts and the order that they should be displayed in

	# Keeps track of all the posts to prevent them from being displayed again (eg. if two keywords are in the same post)
	post_list = [] 

	for keyword in keyword_list: 
		# For each keyword that the user has chosen, the pid, title, body, pdate, poster, keyword count, vote count, and
		# answer count (zero if no answers) will be executed
		# NOTE: In this attempt, I used the following statement below to only determine the keyword count. However, I left the 
		# statement below as it is (with the other information such as pid, title, body, etc) in case I want to refer back
		# to it.
		c.execute("""SELECT p_count.pid, p_count.title, p_count.body, p_count.pdate, p_count.poster, COUNT(p_count.pid) AS pcount, 

					IFNULL(v_count.vcount,0) AS vcount, a_count.acount AS acount
				 
					FROM (SELECT posts.pid , posts.title, posts.body, posts.pdate, posts.poster from posts where title LIKE ?

					UNION ALL

					SELECT posts.pid, posts.title, posts.body, posts.pdate, posts.poster from posts where body LIKE ?

					UNION ALL
	
					SELECT tags.pid, posts.title, posts.body, posts.pdate, posts.poster from tags, posts 

					where tags.pid = posts.pid AND tag LIKE ?) p_count
					
					LEFT OUTER JOIN (SELECT v.pid, COUNT(v.vno) as vcount FROM votes v GROUP BY v.pid) v_count
				
					ON p_count.pid = v_count.pid LEFT OUTER JOIN 
					
					(SELECT a.qid, COUNT(a.pid) AS acount 
					
					FROM answers a GROUP BY a.qid) a_count ON p_count.pid = a_count.qid
					
					GROUP BY p_count.pid
					
					ORDER BY pcount DESC

					;""", (keyword, keyword, keyword,)) 

		# ----------------------------------------------
		# The following is used to determine the order that the posts will be displayed in (based the number of keywords
		# that show up in each result)
		row = c.fetchall()
		for each in row:
			order_track.append((each['pid'],each['pcount']))  
			# Used to keep track of the postID and the keyword count
			# eg. [(pid: 001, pcount: 3), (pid: 002, pcount: 2)]

		order_track.sort(key =lambda order_list: order_list[1], reverse = True)
		# Sorts the list based on the keyword count, or the second element of each tuple (in descending order)
		# eg. Taken from the example above, [(pid: 001, pcount: 2), (pid: 002, pcount: 3)]
		# -------------------------------------------------
	
	select_options = {} 
	# Will be used to keep track of the post that the user has selected.
	# eg. {'1': p005, '2': p006}
	# If the user enters '1' as their input later on, then 'p005' will be returned


	# Will store how many posts will be displayed at one time (eg. the first time, 5 posts will be displayed, and 10 posts will
	# be displayed for the second time).
	max = 0 
	selected = False # The user has not selected a post yet
	reached_max = False # Did not display all the posts yet

	# ----------------------------------------------------------------------
	# The following will group the keyword count for posts with the same keyword together 
	# (eg. post1 has 2 keyword1, post1 has 3 keyword2, therefore post1 will have a total keyword count of 5)

	temp_dict = {} # Temporary dictionary

	for tup in order_track:
		temp_dict[tup[0]] = 0 # Each post id wil act as a key and  will start off with a keyword count of 0 intiially

	for key in temp_dict.keys(): 
		for tup in order_track:
			if tup[0] == key: # Check if each post id occurs more than once, and if it does, add the keyword counts together
				temp_dict[tup[0]] += tup[1]

	order_track = list(tuple(temp_dict.items())) # Order track will become a list of tuples again
	order_track.sort(key =lambda order_list: order_list[1], reverse = True) # In descending order again
	
	# ----------------------------------------------------------------------

	while not selected:
		max += 5 # Determines how many posts will be displayed
		for num in range(max):
			try:
				current = order_track[num][0] # Order track in the form of eg. [('p001', 5), ('p008', 2)]
			except IndexError: 
				reached_max = True
				 # Posts will be displayed in multiples of 5. Ignore error if it is not a multiple of 5 (eg. 13 posts)
				
			# For each post from the ordered list (order_track), its information will be displayed.
			# Creating an similar execute statement again to see if it would work better
			c.execute("""SELECT p.pid, p.title, p.body, p.pdate, p.poster, 

					IFNULL(v_count.vcount,0) AS vcount, a_count.acount AS acount
				 
					FROM posts p
					
					LEFT OUTER JOIN (SELECT v.pid, COUNT(v.vno) as vcount FROM votes v GROUP BY v.pid) v_count
				
					ON p.pid = v_count.pid LEFT OUTER JOIN (SELECT a.qid, COUNT(a.pid) AS acount 
					
					FROM answers a GROUP BY a.qid) a_count ON p.pid = a_count.qid WHERE p.pid = ?""", (current,))

	   
			display = c.fetchall()

			for each in display:
				if each['pid'] not in post_list: # If the post has not been displayed yet (in case of multiples of the same post)
					print('----------------')
					post_list.append(each['pid']) # Keeps track of posts that have already been posted
			
					print('Result ' + str(num+1) + '\n\n' + 'postID: ' + each['pid'] + '\n' + 'Title: ' + each['title'] + '\n' + 
						'Date: ' + each['pdate'] + '\n' + 'Poster: ' + each['poster'] + '\n' +
						'Number of votes: '+ str(each['vcount']) + '\n' + 
						'Number of answers: ' + str('N/A' if each['acount'] == None else each['acount']) + '\n' + 'Body: ' + 
						each['body'][:30] + '...') # If the post is an answer, then the number of answers is N/A.

					select_options[str(num+1)] = each['pid'] # Add the post option into the list of possible options for user

		if not reached_max: # If more posts can be displayed			
			user_select = input("\nSelect a post displayed above, or type in 's' to see more posts. \n")
		else:
			user_select = input("\nSelect a post displayed above:  \n")


		if user_select in select_options.keys(): # If the user selects a post result number that is displayed above
			return select_options[user_select]



	conn.commit()

	conn.close()


keyword_search() 
