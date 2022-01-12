import pymongo
srv2 = "mongodb+srv://username:password@hostname/dbname?retryWrites=true&w=majority"
client = pymongo.MongoClient(srv2,tlsAllowInvalidCertificates=True)
print(client.list_database_names())
mydb = client["test"]
mycol = mydb["test-coll"]
x = mycol.find_one()
print(x)