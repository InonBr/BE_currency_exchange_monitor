import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
DB = client["stocks"]
COLLECTION = DB["stocks_collection"]


def upload_to_db(list_of_dic):
    for stock in list_of_dic:
        COLLECTION.replace_one({"name": stock["name"]}, stock, upsert=True)
