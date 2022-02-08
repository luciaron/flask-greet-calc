# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

from operations import add, sub, mult, div

@app.route('/add')
def add_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a,b))

@app.route('/sub')
def sub_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a,b))

@app.route('/mult')
def mult_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a,b))

@app.route('/div')
def div_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a,b))

operators = { #need to define this because op variable below will be a string, so this allows us to get the variables by keying them to their relative strings in a dictionary
  "add" : add,
  "sub" : sub,
  "mult": mult,
  "div" : div
}

@app.route('/math/<op>')
def math(op):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operators[op](a,b))