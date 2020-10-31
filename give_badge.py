import sqlite3, sys
from datetime import date
""" -----------------------
Purpose: Allows the privileged user to give the poster a badge. 

Input: postID
Output: None
---------------------------"""
def give_badge(post_id):

	conn = sqlite3.connect(sys.argv[1]) # Pass the database as a command line argument
	conn.row_factory = sqlite3.Row 
	c = conn.cursor()
	c.execute('PRAGMA foreign_keys = ON;')
	
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

	c.execute('INSERT INTO ubadges VALUES (:uid, :bdate,:b_name)', b_add)
	print('\nBadge has been given!')

	conn.commit()

	conn.close()
