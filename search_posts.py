'''Search for posts.The user should be able to provide one or more keywords, 
    and the system should retrieve all posts that contain at least one keyword either in title, body, or tag fields.
        
    For each matching post, in addition to the columns of posts table, the number of votes, and the number of 
    answers if the post is a question (or zero if the question has no answers) should be displayed. 

    The result should be ordered based on the number of matching keywords with posts matching the 
    largest number of keywords listed on top. If there are more than 5 matching posts, 
    at most 5 matches will be shown at a time, letting the user select a post or see more matches. 
    The user should be able to select a post and perform a post action (as discussed next).'''

    
# TO DO:
# Figure out how to get the function to work for more than one keyword
# Consider possible test cases
# Providing a description about the function 
# Display the result differently for questions and answers (do not leave as NULL) (as mentioned in forum)



import sqlite3, sys
from datetime import datetime

conn = sqlite3.connect(sys.argv[1]) # Pass the database as a command line argument
conn.row_factory = sqlite3.Row 
c = conn.cursor()
c.execute('PRAGMA foreign_keys = ON;')



def ask_for_keywords():
	keyword_list = []
	search_keyword = True

	while search_keyword: 
		user_input = '%' + input('\nEnter one or more keywords to narrow down your search: ') + '%'
		keyword_list.append(user_input)
		continue_search = input('\n Would you like to enter another keyword? (y/n)?: ')

		if continue_search == 'n': # If the user no longer wants to enter any more keywords
			search_keyword = False

	return keyword_list

def keyword_search(keyword_list): 
	for keyword in keyword_list: # Add the rest of the columns later***
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

					;""", (keyword, keyword, keyword,)) # Still working on changing its order***

		# Displaying the results
	not_selected_post = True # User has not selected a post yets
	display_pcount = 5
	p_num_count = 1
	post_dict = {}

	while not_selected_post:
		row = c.fetchmany(display_pcount)
		for p_num, each in enumerate(row, start = p_num_count):
			print('\n', p_num,each['pid'], each['title'], each['body'][:50] + '...', each['pdate'], each['poster'], each['pcount'], 
			each['vcount'], each['acount'], '\n')
			post_dict[str(p_num)] = each['pid']
		p_num_count += 5
		print(post_dict)

		if len(row) == display_pcount:
			user_action = input("Select one of the following posts, or type in 's' to see more.")
			if user_action in post_dict.keys():
				user_action = post_dict[user_action]
				print(user_action)
				return user_action
		else:
			user_action = input("Select one of the following posts.")
			if user_action in post_dict.keys():
				user_action = post_dict[user_action]
				print(user_action)
				return user_action

keyword_list = ask_for_keywords()
keyword_search(keyword_list)

conn.commit()

conn.close()



