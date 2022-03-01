import pymongo

if __name__ == '__main__':
    # client = pymongo.MongoClient("")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # print(client)
    
    db = client['pymongo-test']     # DB name
    collection = db['test-1']       # Create Collection named test-1 inside DB

    # Delete One Document
    # collection.delete_one({"version": 1.21})
    # print("Successfully Deleted.")

    # Delete Many Documents
    # down = collection.delete_many({"name": "sklearn"})
    # print("Deleted All Occurrences Successfully.")
    # print("Deleted Occurences Count: "+ str(down.deleted_count))

    # Delete All Documents inside Collection
    # down = collection.delete_many({})
    # print("Entire Data inside Collection Deleted Successfully.")

    # Delete Entire Collection ```⚠️⚠️Don't Try in Production Ready Code```
    # collection.drop()
    # print("Deleted Collection Successfully.")

