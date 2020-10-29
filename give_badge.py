# Post action-Give a badge. The user can give a badge to the poster by providing a badge name. 
# The information is recorded in the database with the badge date set to the current system date. [PRVILEGED]

# TO DO:
# Consider possible test cases
# Providing a description about the function 

def give_badge(post_id):
	import sqlite3, sys
	from datetime import date

	conn = sqlite3.connect(sys.argv[1]) # Pass the database as a command line argument
	conn.row_factory = sqlite3.Row 
	c = conn.cursor()
	c.execute('PRAGMA foreign_keys = ON;')
	

	current = date.today() # The current date 


	c.execute('SELECT poster FROM posts WHERE pid = ?;', (post_id,))
	row = c.fetchone()
	poster_id = row['poster'] # Find the poster of the selected post
	
	c.execute('SELECT rowid, bname FROM badges ORDER BY rowid; ') # rowids are used to give numbered options to the user
	row = c.fetchall()
	for b_info in row:
		print(b_info['rowid'],b_info['bname']) # Displaying the badge options for the user to choose from

	# User enters a number that corresponds to the badge name
	b_name_input = int(input('Which badge would you like to give? Enter the number that is associated with the badge: '))

	for each in row:
		if each['rowid'] == b_name_input:
			b_name_input = each['bname'] # Finds the badge name based on the number given by the user


	b_add = {'uid': poster_id, 'bdate': current, 'b_name': b_name_input} 
	# A unique constraint error (on id and date) when giving a badge to the same user on the same day?? ***

	c.execute('INSERT INTO ubadges VALUES (:uid, :bdate,:b_name)', b_add)

	conn.commit()

	conn.close()

# give_badge('p007') 