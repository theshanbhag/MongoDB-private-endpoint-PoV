# Connecting Google Private service connect with MongoDB atlas.
**MONGODB INC. INTERNAL ONLY - DO NOT PROVIDE THIS PROJECT'S CONTENT DIRECTLY TO PROSPECTS, CUSTOMERS OR THE PUBLIC COMMUNITY**

### Pre-requisites for PoV:

GCP:
1. Access to GCP console with permissions to add/update VPC network to
Create a subnet with at least 50 free IP addresses.
2. Enable the API for Service Directory by navigating to GCP console -> Network services -> Service Directory.

MongoDB:
1. Admin Access to MongoDB Atlas to create a MongoDB cluster with cluster tier M10 or higher. (Please use GETATLAS to get free credits for running the PoV). 

**Note**: The Private Endpoints are available only for dedicated clusters i.e. M10 or higher.

Atlas PSC setup for **Replica set**:
1. Log-on to your Atlas account and navigate to your project.
2. Create a Dedicated cluster with tier M10 or above. Do not enable sharding for this cluster if using M30+ clusters. Ensure you are using MongoDB version 4.x+ for this PoV.
3. In the project's Security tab, choose to add a new user, e.g. adminuser, and for User Privileges specify Read and write to any database (make a note of the password you specify).
4. We are not using any external IP address. We don't need to whitelist any IP address as such. (In shared project - Do not delete any ip whitelisted). 
5. Navigate to **Private Endpoints** tab in **Network Access** and click on Add Private endpoint.  
    ><
    ![Valid Document](img/atlas01.png "Valid Document")
    Select Google Cloud and Click Next.
    ![Valid Document](img/atlas02.png "Valid Document")
    Choose a region. (Preferably : The region should be same as the region of the Application)
    ![Valid Document](img/atlas03.png "Valid Document")
    Once you create Next the private endpoints will get created.
    ![Valid Document](img/atlas04.png "Valid Document")
    Once your Atlas Endpoint Service is ready, you will be able to create your Private Service Connect endpoints in your Google Cloud project using the Google Cloud CLI . When you create Private Service Connect endpoints, you specify a subnet in your VPC network; you may either create a new subnet to encapsulate your endpoints or use an existing one. Fill in your GCP project and VPC details (Read through the instructions by expanding the instructions on the same page).
6. Install gcloud command line utility on your workstation. Copy the commands from popup on Atlas and save it as shell script and run using the shell command.
7. Once the script completes running it will generate a Json file in the same location with name atlasEndpoints-<name of your psc>.json
8. Upload the file using Upload file button on Next screen. 
9. Wait and check for the Endpoint status to change to Completed.

![Valid Document](img/atlas05.png "Valid Document")
Atlas creates 50 service attachments for your google private service connect private endpoint. Each endpoint provided is attached to service attachment to enable private connectivity.

