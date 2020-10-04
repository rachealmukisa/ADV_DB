
# A very simple Bottle Hello World app for you to get started with...

import os
import sqlite3
from bottle import get, post, template, request, redirect

#are we executing at PythonAnywhere?
ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ

#assert ON_PYTHONANYWHERE == True

if ON_PYTHONANYWHERE:
    #on PA, set up to connect to WSGI server
    from bottle import default_app
else:
    #on the development environment, import the development server
    from bottle import run, debug

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

if ON_PYTHONANYWHERE:
    #on PA, connect to WSGI server
    application = default_app()
else:
    #on the development environment, run the development server
    debug(True)
    run(host='localhost', port=8080)