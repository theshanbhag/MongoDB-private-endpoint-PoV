import pymongo
srv2 = "mongodb+srv://venkatesh:ashwin123@cluster0-pl-0-us-east1.t6hqq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(srv2,tlsAllowInvalidCertificates=True)
print(client.list_database_names())
mydb = client["test"]
mycol = mydb["test-coll"]
x = mycol.find_one()
print(x)