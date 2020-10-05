import sqlite3

connection = sqlite3.connect("users.db")
#create a cursor
cursor = connection.cursor()
cursor.execute("SELECT * FROM users")
result = cursor.fetchall() 
print(result)

