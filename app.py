from flask import Flask,request
from data import store
from pages import home

app = Flask(__name__)

@app.get("/test")
def hello_world():
    return {"data":store}


@app.post("/store/<string:name>")
def add_data(name):
    return {"message": "Store not found"}, 404


#sends the pages  data off to you.
@app.route("/pages/about", methods=['GET'])
def sendAbout():
    return {"data":[]}, 201


@app.route("/pages/projects", methods=['GET'])
def sendProjects():
    return {"data":[]}, 201


@app.route("/pages/contact", methods=['GET'])
def sendContacts():
    return {"data":[]}, 201

@app.route("/pages/home", methods=['GET'])
def send_home_data():
    print(request.method)
    return {"data":[]}, 201


@app.route("/resume", methods=['GET'])
def sendResume():
    return {"data":[]}, 201


