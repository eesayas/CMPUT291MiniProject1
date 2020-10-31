# Post action-Vote. The user should be able to vote on the post (if not voted already on the same post). The vote should be recorded in the 
# database with a vno assigned by your system, the vote date set to the current date and the user id is set to the current user.

# TO DO:
# Consider possible test cases
# Providing a description about the function 


import sqlite3, sys
from datetime import date

conn = None
c = None
def vote(user_id,post_id):
    current = date.today()
    print(current)
    #this makes sure the post exists
    c.execute("SELECT * FROM posts p1 WHERE p1.pid=:ourPid",{"ourPid":post_id} )
    rows = c.fetchall()
    if len(rows) < 1:
        print("This post does not exist. Vote rejected")
        conn.commit()
        #conn.close()
        return
    #this makes sure the user has not already voted on this specific post
    c.execute("SELECT pid FROM votes WHERE pid =:ourPid AND uid=:ourUser",{"ourPid":post_id, "ourUser":user_id} )
    rows = c.fetchall()
    if len(rows) > 0:
        print("You have already voted on this post. Vote rejected")
        conn.commit()
        #conn.close()
        return
    c.execute("SELECT DISTINCT vno FROM votes")
    rows = c.fetchall()
    max = 0
    num = len(rows)
    print(num)
    for i in range(0, num):
        if rows[i][0] > max:
            max = rows[i][0]
    print(max)
    newVn = max +1
    conn.commit()

    c.execute("INSERT INTO votes VALUES (:ourPid, :ourVn, :ourVoteDate, :ourUser);", {'ourPid': post_id, 'ourVn': newVn, 'ourVoteDate': current, 'ourUser': user_id})
    
    conn.commit()


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

    c.execute(drop_answers)
    c.execute(drop_questions)
    c.execute(drop_votes)
    c.execute(drop_tags)
    c.execute(drop_posts)
    c.execute(drop_ubadges)
    c.execute(drop_badges)
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

    c.execute(users_query)
    c.execute(badges_query)
    c.execute(ubadges_query)
    c.execute(posts_query)
    c.execute(tags_query)
    c.execute(votes_query)
    c.execute(questions_query)
    c.execute(answers_query)

    return


def insert_data():
    global conn, c

    insert_courses = '''
                        INSERT INTO course(course_id, title, seats_available) VALUES
                            (1, 'CMPUT 291', 200),
                            (2, 'CMPUT 391', 100),
                            (3, 'CMPUT 101', 300);
                    '''

    insert_students = '''
                            INSERT INTO student(student_id, name) VALUES
                                    (1509106, 'Jeff'),
                                    (1409106, 'Alex'),
                                    (1609106, 'Mike');
                            '''

    c.execute(insert_courses)
    c.execute(insert_students)
    conn.commit()
    return

def connect(path):  
    global conn, c
    conn = sqlite3.connect(path) # Pass the database as a command line argument
    conn.row_factory = sqlite3.Row 
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON;')
    conn.commit()
    return


def main():
    global connection, cursor
    connect(sys.argv[1])
    #drop_tables()
    #define_tables()
    #c.execute('''insert into users(uid,name,pwd,city,crdate) VALUES ('u001','Vince Wain', 123, 'Edmonton', 2019-01-05);''')
    #c.execute('''insert into posts(pid,pdate,title,body,poster) VALUES ('p001',2019-01-06, 'What can I do to earn badges?', 'What kind of posts do people tend to give out badges for?','u001');''')
    vote('u001','p001')
    conn.commit()
    conn.close()

main()
