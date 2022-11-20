from flask import Flask
from data import store

app = Flask(__name__)

@app.get("/test")
def hello_world():
    return {"data":store}


@app.post("/store/<string:name>")
def add_data(name):
    return {"message": "Store not found"}, 404


#sends the pages  data off to you.
@app.route("/pages/about", methods=['GET'])
def sendPages():
    return {"data":[]}, 201


@app.route("/pages/projects", methods=['GET'])
def sendPages():
    return {"data":[]}, 201


@app.route("/pages/contact", methods=['GET'])
def sendPages():
    return {"data":[]}, 201

@app.route("/pages/home", methods=['GET'])
def sendPages():
    return {"data":[]}, 201


@app.route("/resume", methods=['GET'])
def sendPages():
    return {"data":[]}, 201


