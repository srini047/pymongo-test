import pymongo

def connectClient():
    # client = pymongo.MongoClient("")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # print(client)
    return client
