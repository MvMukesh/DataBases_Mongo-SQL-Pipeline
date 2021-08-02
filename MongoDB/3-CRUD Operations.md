# Primary Commands
  * run mongod => /users/mvon/mongodb/bin/mongod --dbpath /Users/mvon/mongodb_data
  * open mongo => /users/mvon/mongodb/bin/mongo   => start giving commands 
  * stop => ctrl + C in shell [https://docs.mongodb.com/manual/tutorial/manage-mongodb-processes/#use-kill]
----

># `Creating DB & Collections`

Command | Work
------ | --------
![image](https://user-images.githubusercontent.com/26667491/127486180-65e03a7f-e014-4531-ae38-e98c15723bc3.png) | list all dbs within surver 
![image](https://user-images.githubusercontent.com/26667491/127486265-fd883bd2-1ffd-40be-9bf3-becd75cb6c33.png) | use local db 
![image](https://user-images.githubusercontent.com/26667491/127486318-7a6ea2c8-1427-464e-adf6-ea80f48215d3.png) | create new db (db is not shown untill contain atleat one col.)  
![image](https://user-images.githubusercontent.com/26667491/127486667-cf09ab31-4c3a-4d5b-a363-1c346773b480.png) | create new collection implicitly [db is object of current database names as demo, user is collection name, inside {} brackets is document] 
![image](https://user-images.githubusercontent.com/26667491/127487922-a015b5b9-cfe0-4429-8931-87f40593bf5b.png) | check which db we are working on 
![image](https://user-images.githubusercontent.com/26667491/127486930-e2203403-28b9-4335-bc45-11749f3d0b49.png) | shows all collection inside db
![image](https://user-images.githubusercontent.com/26667491/127487347-1def44f9-fe7c-45c1-8a08-e84c0c4d6762.png) | create new collection `explicitly`
![image](https://user-images.githubusercontent.com/26667491/127488475-5525843b-46de-4777-9e6f-e05640c659f3.png) | `Creating Databases`
![image](https://user-images.githubusercontent.com/26667491/127488566-e25df411-6d86-48e7-be42-7d9d56b1ac1b.png) | `Creating Collections`

---

># `Inserting Documents`

Command | Output
---- | ------
`Insert Single Document`  | ![image](https://user-images.githubusercontent.com/26667491/127490435-201407b2-ce8d-4ad1-9ef6-8d495fcd6577.png)
`Insert Multiple Document` | ![image](https://user-images.githubusercontent.com/26667491/127490513-0ffd2afd-9d32-4725-ac8d-31d7d582ff14.png)

---

># `Reading Document`

Command | Output
------  | -------
![image](https://user-images.githubusercontent.com/26667491/127491149-a25e5c16-59be-4003-b162-bfc5ccf081a9.png) | `reading all document in collection`
![image](https://user-images.githubusercontent.com/26667491/127491255-9061a83d-217a-4f5b-be89-ee724668e8f5.png)![image](https://user-images.githubusercontent.com/26667491/127491925-4d1da4d0-d364-4a0b-a699-282fefc1343e.png) | `reading one document in collection`


---

># `_id Field` 
>primary key for document 
>unique all time (generate implicetly if not given)

Command | Output
------  | -------
ObjectId("6107b4b69a6be9cbce5c5996") <= hexadecimal field contain time stamp values => values for creation of this doc, a randome value and an incrementing counter value to uniquelly identify this document ==>> acts as a primary key for this document| ![image](https://user-images.githubusercontent.com/26667491/127835010-58f8e282-eba4-43b6-af85-73573a8594af.png)
![image](https://user-images.githubusercontent.com/26667491/127492253-7ce3b682-e9aa-43aa-93a3-2cd52214b917.png) | ![image](https://user-images.githubusercontent.com/26667491/127492276-ab4115f7-79ba-4b88-aa54-7933b0168729.png)
![image](https://user-images.githubusercontent.com/26667491/127492330-5fa52760-f332-428b-a8a9-c71ce1078600.png) | ![image](https://user-images.githubusercontent.com/26667491/127492377-50913795-3928-41af-bd4a-0c6313184f88.png)
![image](https://user-images.githubusercontent.com/26667491/127492505-e8d211ee-34cf-4978-b325-dea7c3f26297.png) | ![image](https://user-images.githubusercontent.com/26667491/127492531-93435451-3bd0-4626-855e-47f87669bab8.png)
![image](https://user-images.githubusercontent.com/26667491/127493189-2d327a68-0b0c-4d5e-b452-0a1309a0eb3b.png) | ![image](https://user-images.githubusercontent.com/26667491/127493218-020fd2a4-6f08-4bd6-990d-0a164c9b1d1f.png)![image](https://user-images.githubusercontent.com/26667491/127493256-d8b09a59-f22b-48b1-a748-e1485fcaecb6.png)

---

># `Importing Data`
Command | Output
------  | -------
![image](https://user-images.githubusercontent.com/26667491/127493591-2b18462a-108b-482b-b8bf-08e08c6fac88.png) | ![image](https://user-images.githubusercontent.com/26667491/127493657-79842623-d462-464b-a459-a3c6e67f664b.png)
![image](https://user-images.githubusercontent.com/26667491/127493737-6204aec1-45cc-4413-97a4-dfa64b5b6036.png) | ![image](https://user-images.githubusercontent.com/26667491/127493798-cfa35bc1-998f-484a-91ff-0a163bd6ba96.png)
![image](https://user-images.githubusercontent.com/26667491/127493826-c25ceb76-44ee-41a1-81a6-3936554b9503.png) | ![image](https://user-images.githubusercontent.com/26667491/127493962-ff43d391-b185-4cdd-a41b-658b646aa440.png)

# `Exporting Data`
Command | Output
------  | -------
![image](https://user-images.githubusercontent.com/26667491/127494191-23b67cdc-0293-4ae6-805c-7df6e7744663.png) | ![image](https://user-images.githubusercontent.com/26667491/127494238-9b7cf434-e964-4905-9631-6f1979303b9d.png)
![image](https://user-images.githubusercontent.com/26667491/127494255-51ba9217-8a04-43cc-b9b8-badcbeb79529.png) | ![image](https://user-images.githubusercontent.com/26667491/127494290-4223e676-ac8e-44c7-a6cf-a2dbc3ae7f44.png)

---

># `Backup and Restore`
Command | Output
------  | -------
Taking Backup of Database | ![image](https://user-images.githubusercontent.com/26667491/127495370-89053cb2-8828-4383-84e4-93cae09cef00.png)
Restoring from Backup DataBase | ![image](https://user-images.githubusercontent.com/26667491/127495407-1c15a32a-3c6f-47f0-b673-581c8255f9e2.png)

---

># `Updating Documents`
Command | Output
------  | -------
Updating a single document | ![image](https://user-images.githubusercontent.com/26667491/127503282-76611b25-59c3-4548-969c-9be549bd3c06.png)
Updating multiple documents | ![image](https://user-images.githubusercontent.com/26667491/127503315-ab707b1b-a56e-4fee-b7e6-1e764a8bb9fa.png)
Update operators | ![image](https://user-images.githubusercontent.com/26667491/127503850-430f9951-4e3c-4e42-8a1a-e013142356e4.png)![image](https://user-images.githubusercontent.com/26667491/127503562-36f53725-4cbf-4538-a982-9d3aa224b913.png)
Complete list of update operators | [https://docs.mongodb.com/manual/reference/operator/update-field/]
Update multiple fields together | ![image](https://user-images.githubusercontent.com/26667491/127504097-639977cf-e51c-4e2c-b186-22454352d147.png)

---

># `Deleting`
Command | Output
------  | -------
Deleting field(s) within a document | ![image](https://user-images.githubusercontent.com/26667491/127504392-4c094ca8-562d-4600-994f-2bc206619a6f.png)
Deleting document(s) | ![image](https://user-images.githubusercontent.com/26667491/127504480-23617ae1-4620-463d-ade5-ba6fd6d60e9d.png)
Deleting collection | ![image](https://user-images.githubusercontent.com/26667491/127504553-58310402-c243-4a54-8a1e-d4762399243e.png)
Deleting database | ![image](https://user-images.githubusercontent.com/26667491/127504612-5d7fe011-e62e-476e-9dbc-885ab0f4c497.png)







