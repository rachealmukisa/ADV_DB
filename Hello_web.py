from bottle import route, run, template

@route('/hello')
@route('/hello/<my_name>')
def get_hello(my_name):
    return template("Hello {{name}}!", name=my_name)

@route('/goodbye')
def get_goodbye():
    return "<html>Goodbye there!!!</html>"

run(host='localhost', port=8080)



""" from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/say')
def say():
    return "<html>Say Here!!!</html>"

run(host='localhost', port=8080) """