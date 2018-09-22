from flask import Flask,jsonify, url_for
from flask_restful import reqparse, request

from server import webcms3
from enum import Enum, unique, IntEnum
import json


app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
	orderList = list()
	return jsonify(orderList)

@app.route("/detail/<cID>", methods=['GET'])
def detail(cID):
	json = webcms3.get_course_outline('undergraduate',cID, 2018)
	return jsonify(json)

@app.route("/resource/<cID>", methods=['GET'])
def resource(cID):
	json = webcms3.get_leture_resoucre('COMP9319')
	return jsonify(json)

@app.route("/download/<cID>", methods=['GET','POST'])
def download(cID):
	content = request.json
	result = webcms3.download(content['zid'], content['zPassword'], cID)
	print(result)
	return jsonify(result)

if __name__ == "__main__":
	app.config['JSON_AS_ASCII'] = False
	app.debug = True
	app.run()