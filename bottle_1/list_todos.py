import sqlite3

connection = sqlite3.connect("todo.db")
#create a cursor
cursor = connection.cursor()
cursor.execute("SELECT * FROM todo")
result = cursor.fetchall() 
print(result)

