from flask import jsonify, request
from flask_pymongo import PyMongo
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/checkingTheTime")
db = mongodb_client.db


@app.route('/', methods=['GET'])
def home():
    return "I'm just an API"


@app.route('/watches/api', methods=['GET'])
def getapi():
    data = []
    for watch in db.watches.find():
        watch['_id'] = str(watch['_id'])
        data.append(watch)
    return jsonify(data)


app.run()
