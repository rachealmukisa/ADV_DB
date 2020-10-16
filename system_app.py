# A very simple Bottle Hello World app for you to get started with...

import os
import sqlite3
from bottle import get, post, template, request, redirect

# are we executing at PythonAnywhere?
ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ

# assert ON_PYTHONANYWHERE == True

if ON_PYTHONANYWHERE:
    # on PA, set up to connect to the WSGI server
    from bottle import default_app
else:
    # on the development environment, import the development server
    from bottle import run, debug

from storage import get_users, get_user, update_status, create_user, update_user, delete_user


@get('/')
def get_show_list():
    result = get_users()
    return template("show_list", rows=result)


@get("/set_status/<id:int>/<value:int>")
def get_set_status(id, value):
    update_status(id, value)
    redirect("/")


@get("/new_user")
def get_new_user():
    return template("new_user")


@post("/new_user")
def post_new_user():
    f_name = request.forms.get("f_name").strip()
    myemail = request.forms.get("myemail").strip()
    msg = request.forms.get("msg").strip()
    #new_user = request.forms.get("new_user")#.strip()
    create_user(f_name, myemail, msg)
    redirect("/")


@get("/update_user/<id:int>")
def get_update_user(id):
    result = get_user(id)
    return template("update_user", row=result)


@post("/update_user")
def post_update_user():
    id = int(request.forms.get("id").strip())
    updated_f_name = request.forms.get("f_name").strip()
    updated_myemail = request.forms.get("myemail").strip()
    updated_msg = request.forms.get("msg").strip()
    update_user(id, updated_f_name, updated_myemail, updated_msg)
    redirect("/")


@get("/delete_user/<id:int>")
def get_delete_user(id):
    delete_user(id)
    redirect("/")

if ON_PYTHONANYWHERE:
    # on PA, connect to the WSGI server
    application = default_app()
else:
    # on the development environment, run the development server
    debug(True)
    run(host='localhost', port=8080)


