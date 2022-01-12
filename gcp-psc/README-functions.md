## Connecting to Atlas from a google cloud Functions using PSC:

1. Enable cloud functions API on GCP by navigating to cloud functions. 
2. Create a subnet in the same VPC network as that of the PSC. 
```Note : the subnet ip ranges should have /28 mask and should reside in same region as that of the PSC.```
3. Create Serverless VPC that will allow Cloud Functions, Cloud Run (fully managed) services and App Engine standard environment apps to access resources in a VPC network using those resources private IPs. 
4. Navigate to cloud functions and create a new cloud function. Allocate appropriate resources from RUNTIME tab. Select the VPC connector created in step 3 and fill in the CONNECTIONS tab. Click on Next. 
5. Navigate to clusters and select the cluster that is deployed on the same region as that of the PSC. Click on connect > Private Endpoints (Connection Types) > connect your Application > Copy the SRV string into the script you will run on the VM instance.
6. Select your choice of programming language. We have selected python for this demo. Below is the snippet of code for main.py file (This is only Sample code to test the mongodb Connectivity through GCP cloud functions using PSC).

```doctest
def hello_world(y):
import pymongo
print("Hello World ")
srv2 = "mongodb+srv://username:password@hostname/dbname?retryWrites=true&w=majority"
client = pymongo.MongoClient(srv2,tlsAllowInvalidCertificates=True)
print(client.list_database_names())
mydb = client["test"]
mycol = mydb["test-coll"]
x = mycol.find_one()
print(x)
return "successfully retrives data"
```

6. Update the requirements.txt file as shown below to install pymongo[srv]. Click on deploy. 
7. Test out your function by navigating to cloud function -> your function -> Testing tab -> Click on Test the Function.

