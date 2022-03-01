import pymongo

if __name__ == '__main__':
    # client = pymongo.MongoClient("")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # print(client)
    
    db = client['pymongo-test']     # DB name
    collection = db['test-1']       # Create Collection named test-1 inside DB

    # Insert One Document
    data = {
        # "_id": "621dc995004e4fd5f",
        "name": "sklearn",
        "version": "0.24"
    }

    collection.insert_one(data)

    # Insert Many Documents
    # data_list = [
    #     {"name": "pyMongo", "version": 4.0},
    #     {"name": "Numpy", "version": 1.21},
    #     {"name": "Pandas", "version": 1.3}
    # ]


    # collection.insert_many(data_list)
