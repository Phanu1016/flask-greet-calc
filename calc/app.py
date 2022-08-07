# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route("/add")
def add():
    return str(operations.add(int(request.args["a"]), int(request.args["b"])))

@app.route("/sub")
def sub():
    return str(operations.sub(int(request.args["a"]), int(request.args["b"])))

@app.route("/mult")
def mult():
    return str(operations.mult(int(request.args["a"]), int(request.args["b"])))

@app.route("/div")
def div():
    return str(operations.div(int(request.args["a"]), int(request.args["b"])))

operators = {"add":operations.add, "sub":operations.sub, "mult":operations.mult, "div":operations.div}

@app.route("/math/<operator>")
def math_operator(operator):
    return str(operators[operator](int(request.args["a"]), int(request.args["b"])))