# Backend API-Server


Helping people to Arrange items in an efficient way.


## Installation

Installation is super friendly using `pip`

```
$ pip install 
$ sudo mongod 
$ python app.py

```

## Documentation

* [Test](./test)


This is the layout of the data of json object.
Arrangement JSON Object
## Arrangement: 
## {id: a_,
##  name: _,
##  owner: _,
##  users: [_ids_],
##  items: [_item_objects_],
##  containers: [_container_objects_],
##  is_deleted: _,
##  timestamp: _,
##  snapshots: [_snapshot_objects_]
## }

API routes for /GET and /POST using python and MongoDB. I include the API specs in this document[https://www.evernote.com/client/snv?noteGuid=befbdd2d-de62-4234-b4f9-24e55cedd5ac&noteKey=eeba35063fe77bbb&sn=https%3A%2F%2Fwww.evernote.com%2Fshard%2Fs296%2Fsh%2Fbefbdd2d-de62-4234-b4f9-24e55cedd5ac%2Feeba35063fe77bbb]

Each Containers can have several items for example different kind of car and size.
And inside 

Example of the Arrangement JSON object:

{
    "containers": [
        {
            "id": "cC2CI9MN8", 
            "name": "Jakes van", 
            "size": 8
        }, 
        {
            "id": "cLDJKQ8J1", 
            "name": "nathan van", 
            "size": 8
        }
    ], 
    "id": "aIMBG40VP", 
    "is_deleted": false, 
    "items": [
        {
            "id": "iGH8S90R3", 
            "name": "Jakes", 
            "size": 1
        }, 
        {
            "id": "i7GWRVQIL", 
            "name": "Jakes luggage", 
            "size": 1
        }, 
        {
            "id": "iGN10XW08", 
            "name": "Chin", 
            "size": 1
        }, 
        {
            "id": "i1EWBLGZU", 
            "name": "Nathan", 
            "size": 1
        }, 
        {
            "id": "iWE7MRXXE", 
            "name": "Mikey", 
            "size": 1
        }
    ], 
    "name": "first arrangement", 
    "snapshots": [
        {
            "id": "sDET5Z696", 
            "name": "only snapshot", 
            "snapshot": {
                "cC2CI9MN8": [
                    "i197ZJ4GO", 
                    "i238HYV07", 
                    "i4SLYDFGA"
                ], 
                "cLDJKQ8J1": [
                    "iALRIZBJ1", 
                    "iJBGT7BJF"
                ]
            }
        }
    ], 
    "timestamp": 1537928309.756494
}


## Postman Collection:
https://www.getpostman.com/collections/4755f28c743b47535215

