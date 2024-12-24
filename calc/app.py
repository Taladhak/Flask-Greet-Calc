# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

app.route('/add')
# Added a route for handling addition requests.
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a + b)

app.route('/sub')
# Added a route for handling subtraction requests.
def sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a - b)

app.route('/mult')
# Added a route for handling multiplication requests.
def mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a * b)

app.route('/div')
# Added a route for handling division requests.
def div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(a / b)


  