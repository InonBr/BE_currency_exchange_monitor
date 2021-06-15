import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
DB = client["stocks"]
COLLECTION = DB["stocks_collection"]


def get_all_stocks():
    stocks = COLLECTION.find({}, {"_id": 0})

    return list(stocks)


