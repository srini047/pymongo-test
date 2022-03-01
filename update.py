import pymongo

if __name__ == '__main__':
    # client = pymongo.MongoClient("")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # print(client)
    
    db = client['pymongo-test']     # DB name
    collection = db['test-1']       # Create Collection named test-1 inside DB

    # Update One Document
    # collection.update_one({"name": "sklearn"}, {"$set": {"version": "0.25"}})
    # print("One Document Updated")

    # Update ALl Occurence in Document
    up = collection.update_many({"name": "sklearn"}, {"$set": {"version": 0.24}})
    print("All Document Occurences Updated")
    # print("Number of Occurences Updated: " + str(up.modified_count))    # To view the number of Occurence Updated
