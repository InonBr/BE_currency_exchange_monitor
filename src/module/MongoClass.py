import pymongo


class MongoClass:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # client = pymongo.MongoClient("mongodb://mongo:27017/")
    db = client["stocks"]
    collection = db["stocks_collection"]

    @classmethod
    def upload_to_db(cls, list_of_dic):
        for stock in list_of_dic:
            cls.collection.replace_one({"name": stock["name"]}, stock, upsert=True)

    @classmethod
    def get_all_stocks(cls):
        stocks = cls.collection.find({}, {"_id": 0})

        return list(stocks)
