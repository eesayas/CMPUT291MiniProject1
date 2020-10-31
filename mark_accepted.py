import sqlite3, sys

""" ------------------------------------------------------------
Purpose: If the post is an answer, a privileged user can mark
an answer as the accepted answer, or leave it as it is.

Input: postID that belongs to an answer
Output: None
--------------------------------------------------------------"""

def mark_accepted(post_id):
	conn = sqlite3.connect(sys.argv[1]) # Pass the database as a command line argument
	conn.row_factory = sqlite3.Row 
	c = conn.cursor()
	c.execute('PRAGMA foreign_keys = ON;')

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

	conn.close()





