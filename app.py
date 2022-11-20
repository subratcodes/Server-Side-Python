from flask import Flask
from data import store

app = Flask(__name__)

@app.get("/test")
def hello_world():
    return {"data":store}


@app.post("/store/<string:name>")
def add_data(name):
    return name,201