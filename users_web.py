import os
import sqlite3
from bottle import get, post, template, request, redirect

#are we executing at PythonAnywhere?
ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ

assert ON_PYTHONANYWHERE == False

if ON_PYTHONANYWHERE:
    pass
else:
    #on the development environment, import the development server
    from bottle import run, debug

@get('/')
def get_show_list():
    connection = sqlite3.connect("users.db")
    #create a cursor
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall() 
    cursor.close()
    return template("show_list", rows=result)

@get("/new_user")
def get_new_user():
    return template("new_user")

@post("/new_user")
def post_new_user():
    f_name = request.forms.get("f_name").strip()
    myemail = request.forms.get("myemail").strip()
    msg = request.forms.get("msg").strip()

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    #cursor.execute("insert into users (f_name) values (?,?,?)", (new_user))
    cursor.execute("insert into users (f_name, myemail, msg) values (?,?,?)", (f_name, myemail, msg))
    #cursor.lastrowid
    connection.commit()
    cursor.close()
    #return "The new user is " + new_user + "..."
    redirect("/")

if ON_PYTHONANYWHERE:
    pass
else:
    #on the development environment, run the development server
    debug(True)
    run(host='localhost', port=8080)