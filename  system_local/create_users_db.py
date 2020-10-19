import sqlite3
conn = sqlite3.connect('users.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, f_name varchar(100) NOT NULL, myemail varchar(100) NOT NULL, msg varchar(100))")
conn.execute("INSERT INTO users (f_name, myemail, msg) VALUES ('Angel Lane','angellane@yahoo.com', 'This is my first day')")
conn.execute("INSERT INTO users (f_name, myemail, msg) VALUES ('Jasmin Tomp','jasminet@yahoo.com', 'I look forward to serving')")
conn.execute("INSERT INTO users (f_name, myemail, msg) VALUES ('Caroline Dyna','cdyna@yahoomail.com', 'Dont know why I was given the job')")
conn.execute("INSERT INTO users (f_name, myemail, msg) VALUES ('Brittney Holle','bholle@yahoo.com', 'Like it already')")
conn.commit()