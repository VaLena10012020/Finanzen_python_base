from finanzen_base.Utils.mongoclasses import MongoConnect

def test_MongoConnect_vanilla():
    Mongo_class = MongoConnect()
    assert Mongo_class.collection.full_name == "VaLenaData.Vertraege"
    assert Mongo_class.database.name == "VaLenaData"
    assert Mongo_class.database.client.HOST == "localhost"
    assert Mongo_class.database.client.address == ('localhost',27017)

def test_MongoConnect_collection():
    Mongo_class = MongoConnect(collect='Entgelt')
    assert Mongo_class.collection.full_name == "VaLenaData.Entgelt"