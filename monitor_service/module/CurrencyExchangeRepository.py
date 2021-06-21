import pymongo
from src import get_mongo_url


class CurrencyExchangeRepository:
    mongo_url = get_mongo_url()
    client = pymongo.MongoClient(mongo_url)
    db = client["stocks"]
    collection = db["stocks_collection"]

    @classmethod
    def get_all_stocks(cls):
        stocks = cls.collection.find({}, {"_id": 0})

        return list(stocks)
