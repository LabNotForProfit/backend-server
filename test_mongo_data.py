from flask import Flask, request, jsonify, render_template, json
from pymongo import MongoClient
import pprint
import time

client = MongoClient('mongodb://localhost:27017/')

db = client.test.arrangement1


def get_arrangement_data_from_mongo():
	cursor = db.find()
	for doc in cursor:
		print(doc)
	return doc

	output = []
	for s in doc:
		output.append(s)
	#pprint.pprint(db.find_one())
	return jsonify({'container' : s})


if __name__ == "__main__":
  get_arrangement_data_from_mongo()
