import pymongo
from src import get_mongo_url


class CurrencyExchangeRepository:
    mongo_url = get_mongo_url()
    client = pymongo.MongoClient(mongo_url)
    db = client["stocks"]
    collection = db["stocks_collection"]

    @classmethod
    def upload_to_db(cls, list_of_dic):
        for stock in list_of_dic:
            cls.collection.replace_one({"name": stock["name"]}, stock, upsert=True)
