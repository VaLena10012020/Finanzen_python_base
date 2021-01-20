import pymongo


class MongoConnect:
    def __init__(self, location_name='mongo_transaction', port=27017, db='VaLenaData', collect='Vertraege'):
        self.client = pymongo.MongoClient()
        self.client = pymongo.MongoClient(location_name, port)
        self.database = self.client[db]
        self.collection = self.database[collect]

    def insert_dict(self, document):
        return self.collection.insert_one(document).inserted_id

    def insert_dicts(self, documents):
        ids = []
        for document in documents:
            ids.append(self.collection.insert_one(document).inserted_id)
        return ids

    def get_distinct_item(self, field: str):
        return self.collection.distinct(field)
