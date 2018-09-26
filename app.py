from flask import Flask, jsonify, request
from pymongo import MongoClient
import json
import random
import string
import time

client = MongoClient('mongodb://localhost:27017/')

db = client.test.arrangement

app = Flask(__name__)

@app.route("/")
def home_page():
	return "Arrange That!"


@app.route('/arrangement', methods=['GET'])
def get_arrangement():
	cursor = db.find()
	test_count = cursor.count()
	print(test_count)
	arrangement = cursor.count()
	pass
	# output = []
	# for s in arrangement_id.find():
	# 	output.append({'name' : s['containers']})
	# print(output)
	# return jsonify({'result' : output})

	#arrangement_id = request.args.get("id")

	# if arrangement_id is None:
	# 	pass
	# 	# return all of the arrangement of that user
	# 	#return mongo.db.arrangement.find({"arrangement_id"})
	# else:
	# 	return arrangement_id


@app.route('/arrangement', methods=['POST'])
def add_arrangement():
	pass

# def add_them():
# 	data = {}
#     data["name"] = name
#     data["id"] = create_random_id("a")
#     data["items"] = []
#     data["containers"] = []
#     data["is_deleted"] = False
#     data["snapshots"] = [create_snapshot("only snapshot")]
#     data["timestamp"] = time.time()

# def add_item(name):
# 	item = create_item(name)
# 	data['items'].append(create_item(name))
# 	return item

# def add_container(name, size):
# 	container = create_container(name, size)
# 	data['containers'].append(container)
# 	data['snapshots'][0]['snapshot'][container['id']] = [] 

# def get_container(name):
# 	for container in data['containers']:
#   		if container['name'] == name:
#     return container

# def add_item_to_container(name, container_name):
# 	item = add_item(name)
# 	container_id = get_container(container_name)['id']
# 	data['snapshots'][0]['snapshot'][container_id].append(item['id'])

# @app.route("/arrangement/id")


# @app.route("/user/<username>")
# def user_profile(username):
#     user = mongo.db.users.find_one_or_404({"_id": username})
#     return render_template("index.html",
#         user=user)

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8080, debug = True)
