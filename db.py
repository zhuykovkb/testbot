import datetime

from pymongo import MongoClient

client = MongoClient(host='192.168.2.200', port=27017)

db = client.db1
collection = db.users

user = {"name": "Mike",
        "desc": "My first blog post!",
        "skills": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

users = db.users

user_id = users.insert_one(user).inserted_id

print(user_id)

for user in collection.find():
    print(user)
