from bottle import get, post, run, template, request, redirect
import sqlite3

@get('/')
def get_show_list():
    connection = sqlite3.connect("todo.db")
    #create a cursor
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todo")
    result = cursor.fetchall() 
    cursor.close()
    return template("show_list", rows=result)

@get("/new_item")
def get_new_item():
    return template("new_item")

@post("/new_item")
def post_new_item():
    new_item = request.forms.get("new_item").strip()
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("insert into todo (task, status) values (?,?)", (new_item, 1))
    #cursor.lastrowid
    connection.commit()
    cursor.close()
    #return "The new item is " + new_item + "..."
    redirect("/")

run(host='localhost', port=8080)

"""
# Before the template was modified to show_list
from bottle import route, run, template
import sqlite3

@route('/todos')
def get_todos():
    connection = sqlite3.connect("todo.db")
    #create a cursor
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todo")
    result = cursor.fetchall() 
    cursor.close()
    return template("show_list", rows=result)

run(host='localhost', port=8080)
"""