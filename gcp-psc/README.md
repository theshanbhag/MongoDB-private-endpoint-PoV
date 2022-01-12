# Connecting Google Private service connect with MongoDB atlas.
**MONGODB INC. INTERNAL ONLY - DO NOT PROVIDE THIS PROJECT'S CONTENT DIRECTLY TO PROSPECTS, CUSTOMERS OR THE PUBLIC COMMUNITY**

#### Time to set up:
#### Time to Run:

### Pre-requisites for PoV:

GCP:
1. Access to GCP console with permissions to create/update/delete([Compute Network Admin](https://cloud.google.com/iam/docs/understanding-roles#compute.networkAdmin)) on VPC network to
Create a subnet with at least 50 free IP addresses. Create Custom VPC network and subnet on the region of your preference.
2. Create egress firewall rules permit traffic to the internal IP address of the Google Cloud Private Service Connect endpoint.

MongoDB:
1. Project owner or Organization owner access to MongoDB Atlas to create a MongoDB cluster with cluster tier M10 or higher. (Please use GETATLAS to get free credits for running the PoV). 

**Note**: The Private Endpoints are available only for dedicated clusters i.e. M10 or higher.

### Atlas PSC setup for **Replica set**:
1. Log-on to your Atlas account and navigate to your project.
2. Create a Dedicated cluster with tier M10 or above. Do not enable sharding for this cluster if using M30+ clusters. Ensure you are using MongoDB version 4.x+ for this PoV.
3. In the project's Security tab, choose to add a new user, e.g. adminuser, and for User Privileges specify Read and write to any database (make a note of the password you specify).
4. We are not using any external IP address. We won't whitelist any ip addresses. (In shared project - Do not delete any ip whitelisted). 
5. Navigate to **Private Endpoints** tab in **Network Access** and click on Add Private endpoint.  
    ><
    ![Valid Document](img/atlas01.png "Valid Document")
    Select Google Cloud and Click Next.
    ![Valid Document](img/atlas02.png "Valid Document")
    Choose a region. (The region should be same as the region of the Application or VPC)
    ![Valid Document](img/atlas03.png "Valid Document")
    Once you create Next the private endpoints will get created.
    ![Valid Document](img/atlas04.png "Valid Document")
    Once your Atlas Endpoint Service is ready, you will be able to create your Private Service Connect endpoints in your Google Cloud project using the Google Cloud CLI . When you create Private Service Connect endpoints, you specify a subnet in your VPC network; you may either create a new subnet to encapsulate your endpoints or use an existing one. Fill in your GCP project and VPC details (Read through the instructions by expanding the instructions on the same page).
6. Install [gcloud](https://cloud.google.com/sdk/docs/install) command line utility on your workstation. (Note: Setup your Service account or email with the IAM access specified in pre-requisites. refer gcloud setup [here](https://cloud.google.com/sdk/docs/initializing))
7. Copy the commands shown in the Next screen on Atlas and save it as shell script and run using the shell command.
8. Once the script completes running it will generate a Json file in the same location with name atlasEndpoints-<name of your psc>.json
9. Upload the file using Upload file button on Next screen. 
10. Wait and check for the Endpoint status to change to 'Completed'.

![Network Access](img/atlas05.png "Network Access")
Atlas creates 50 service attachments for your google private service connect private endpoint. Each endpoint provided is attached to service attachment to enable private connectivity.

###Connect to Atlas using Private endpoints:
Note: You must have the MongoDB database in GCP and region must be same as that of the PSC we have created.

The **Private Endpoint** option will be added to your connection type if the creation of the PSC was successful.

![Atlas connect](img/atlas06.png "atlas connect")

Choose **private endpoint** and click on Choose a connection method.

![Atlas connect](img/atlas07.png "atlas connect")

### Connecting to Atlas from a google compute instance using PSC:
1. Create a VM instance satisfying one of the below cases.

#### Cases:
* **Same VPC same subnet:** works. 
* **Same VPC different subnet same region:** works.
* **Same VPC different subnet different region:** Will not work.
* **Different VPC:** Will not work  (on both internal IP only and with external IP).

2. To install python on VM follow [this](https://cloud.google.com/python/docs/setup#linux).
3. SSH into the VM instance and install python dependencies from _requirements.txt_ file. 
```pip3 install -r requirements.txt. ``` 

4. Once the requirements are installed edit the VM and disable the ephemeral ip from network tab.
5. Make a copy of the script either by creating a new python file on VM or by uploading the _run-mongo-script.py_ script file provided in this repo.
6. Update the srv for connecting to your cluster. 
7. Run the python script to connect to MongoDB atlas and access the data.
```python3 run-mongo-script.py```

![GCP ssh](img/gcp_console01.png "gcp_console01")

   ![GCP ssh ](img/gcp_console02.png "gcp_console02")

Note: Make sure you have proper firewall rules setup for accessing the internal ip addresses.

### Execution:
Run python script "run-mongo-script.py" to connect and test the connection from VM to MongoDB Atlas using GCP-PSC. 

### Results:
You  should be able to connect to the MongoDB Cluster using MongoDB client installed on the VM instance and read documents from the cluster without using external IP (Disable the ephemeral IP address on the VM).

### Conclusion
