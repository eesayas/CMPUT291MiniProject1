# Post action-Mark as the accepted. The user should be able to mark the post (if it is an answer) as the accepted answer. 
# If the question has already an accepted answer, the user should be prompted if s/he wants to change the accepted answer. 
# The user can select to change the accepted answer or leave it unchanged.

# TO DO:
# Consider possible test cases
# Providing a description about the function 

def mark_accepted(post_id):
	import sqlite3, sys

	conn = sqlite3.connect(sys.argv[1]) # Pass the database as a command line argument
	conn.row_factory = sqlite3.Row 
	c = conn.cursor()
	c.execute('PRAGMA foreign_keys = ON;')

	# Finding the question ID and the current accepted answer
	c.execute("SELECT a.qid, q.theaid FROM answers a, questions q WHERE a.qid = q.pid AND a.pid = ?", (post_id,))


	row = c.fetchone()
	
	if row['theaid'] != None: # If an accepted answer exists
		acc_answer = row['theaid']  # The pid of the accepted answer
			
		# Gets input from the user if they would like to change the accepted answer
		print("An accepted answer already exists.\n")
		a_exists = input("Would you like to change the accepted answer? \n 1. Yes \n 2. No \n")

	else: # If an accepted answer does not exist
		a_exists = input("Would you like to mark this as the accepted answer? \n 1. Yes \n 2. No \n")



	if a_exists == '1': # If the user wants to change the accepted answer
			# --------------------------------------------------------------------------------
			# If the user is changing the accepted answer to the current accepted answer
			if row['theaid'] == post_id:
					print("This post is already the accepted answer of the question.")
			# --------------------------------------------------------------------------------

			else: # changes the current accepted answer to the answer that the user has chosen
				c.execute("""UPDATE questions SET theaid = ? WHERE pid = 

				         (SELECT a.qid FROM answers a WHERE a.pid = ?)""", (post_id, post_id))


	conn.commit()

	conn.close()

		
mark_accepted('p017')



