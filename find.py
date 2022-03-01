import  pymongo
# from pydantic import ObjectId

if __name__ == '__main__':
    # client = pymongo.MongoClient("")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # print(client)
    
    db = client['pymongo-test']     # DB name
    collection = db['test-1']       # Create Collection named test-1 inside DB

    # Print Entire Collection
    for i in collection.find({}, {"_id": 0}):
        print(i)

    # Find  Single Occurnce
    # print(collection.find_one({"name": "Numpy"}))
    # print(collection.find_one({"name": "Numpy"}, {"name": 1, "_id": 0, "version": 1}))

    # Find All Occurences
    # all_match = collection.find({"name": "sklearn"})
    # # print(type(all_match))
    # for i in all_match:
    #     print(i)
