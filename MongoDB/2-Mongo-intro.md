# Quick Intro to MongoDB

* MongoDB is NoSQL database, follows document based model, designed for ease of development & scalling
  * `Features:` Flexibility, High availability, Horizontal Scalability, Rich query language
---

  1. `Flexibility:` => Document db, Flexible Schema 
      * Store data in a document 
      * Document store data in key:value format much like a dict in python
      * Provides ability to store hierarchy of data within a single document
![image](https://user-images.githubusercontent.com/26667491/127443611-2c943583-3190-4565-90dd-53086c12efab.png)
      * These documents have a flexible schema, meaning that both these documents that have different numbers and types of key value pare
      can exist within same database, thereby providing developers with an ease of development
  
  2. `High availability` => Increasing read capacity, Falt Tolerant
      * High availability of acess to data by its ability of replicatig data
      * Application refer to having multiple databases servers, each mantaining same copy of data
        * These server together make a  `Replica Set`  
        ![image](https://user-images.githubusercontent.com/26667491/127444727-4d5ec55d-215f-465b-aaec-e48558e81ba5.png)
        * One of servers will act as primary & rest will all be secondary
        * When Client interact with replica set, `Write querie` will only be handled by Primary server
        * from there data is replicated to secondary's server but `Read querie` can be handled by any server
        ![image](https://user-images.githubusercontent.com/26667491/127445800-e8e207e0-0290-4a3d-8061-0846e49aa5ac.png)
      * Keeping multiple copies not only allows client to send Read request to any server, but it also `increasing read capacity` of cluster, 
      * also makes it `falt tolerant`, as even if a database server goes down. we have a backup of stored data on a different server
  
  3. `Horizontal Scalability`
      * Possible due to shared data ability, n number of database server can be added as per requirements and by spliting data in small 
      chunks and saving it on n number of database servers this can be seen as `Sharding`
      ![image](https://user-images.githubusercontent.com/26667491/127448112-8acd6103-bbe9-4acd-b488-bb2de0716054.png)
      * and gives MongoDB ability to Execute, Read and Write queries at a much faster rate than on a single server. 
      Each of these servers can have a separate replica of its own. 
      
  4. `Rich Query`    
      * MongoDB provides support for usual 
 ![image](https://user-images.githubusercontent.com/26667491/127448754-4b187772-f98e-4319-a52f-14ad4657dbd5.png)
        * `CRUD operations` [Create, Read, Update, Delete] and also provides 
        * framework for `aggregation of data` like Grouping, Sorting, Filtering etc also provide
        * query operations for `text search` with help of `Regex` and `full text search` and 
        * even `geospatial queries` to efficiently query geospatial or location data. 
---
`Compare RDBMS & MongoDB`
![image](https://user-images.githubusercontent.com/26667491/127448998-6299f032-dc5a-4579-a520-030a0628915d.png)
---

## `Component- MondoDB`
 1. `Documents`
 2. `Collections`
# 1. Documents

MongoDB documnets are similar to Rows in RDBMS
* A MongoDB document is a JSON like document 
  * `JSON or JavaScript Object Notation` is a way to represent and transfer data efficiently. 
    * Example: Lets say we have a pen and a friend wants to know about how it looks. There are two ways to pass on information. First is to package pen and send it so that they can have a firsthand look at it. Second is to describe attributes of the pen so that they can recreate it. That is how JSON works
    * This is how a JSON like document looks like, and this is how MongoDB stores data. 
 ![image](https://user-images.githubusercontent.com/26667491/127457521-ea001281-a065-43d6-8779-dfb9f76c7469.png)
    * Document is stored internally as `BSON document` which stands for `Binary JSON`. 
    * But when you view documents in MongoDB, it is viewed in the `language specific format` 
      * If you're using `Python`, then you view it as `dictionary`
      * If you're using `JavaScript`, then you view it as a `JavaScript Object`

## 1.1 Component of Documents
1.1.1 `Key`s also known as fields
  * Always represented as  String
  * ![image](https://user-images.githubusercontent.com/26667491/127459552-8c19508b-c6ad-4908-a64b-90f6b48cda5a.png)

1.1.2 `Values` corresponde to keys
  * can be String or Numeric or Array or Date or Another Enbedded Document or Sub document which can have any data type within it
  * `Embedded Document` => ![image](https://user-images.githubusercontent.com/26667491/127459810-a36b6db1-7e53-4562-a6c7-dbef1546c31c.png)
  * `Array` => ![image](https://user-images.githubusercontent.com/26667491/127460012-e637ca19-c40c-493d-b1dd-47377a641b96.png)
    * `_id field is bit different` => as it access primary key to uniquely identify document in collection
    * ![image](https://user-images.githubusercontent.com/26667491/127460561-d9f3c440-f46f-436d-8359-381fb917a473.png)

### `Points to Remember while working with Documents`
* While Naming Fields avoid using dot(.) or dollar($) as these r used in MongoDB quary
* Documents r 
  * Type senstive => ![image](https://user-images.githubusercontent.com/26667491/127462092-910f52c3-297b-4d06-ad49-de15374aea76.png) | ![image](https://user-images.githubusercontent.com/26667491/127462211-4c3cfbb4-231b-4821-a8d5-f688b6c094ff.png)
  * Case Senstive => ![image](https://user-images.githubusercontent.com/26667491/127462273-665b5689-9e40-4dd8-a5df-5cbc96ea68d0.png) | ![image](https://user-images.githubusercontent.com/26667491/127462311-6a9325a2-92bd-4e1d-b41f-f8a9546d44a8.png)
  * No duplicate keys => ![image](https://user-images.githubusercontent.com/26667491/127462437-43f8580f-7a78-4d11-bbd2-f56f2bdd415d.png)

## 2. Collections
* Group of MondoDB documents, similar to multiple rows within a Tables in RDBMS
![image](https://user-images.githubusercontent.com/26667491/127463852-cd833d08-ef2c-45a3-92b6-258c20e38a10.png)
 * Row in table correspond to a Document
 * Complete Table correspond to Collection
 * `Flexible Schema`
   * Each document within a Collection can have different Schema![image](https://user-images.githubusercontent.com/26667491/127464750-5c733c9c-c46b-4365-8da5-9e3c7794d4b7.png)
   * as both above documents have different number & type of keys yet they both belong to same Collection - valid in MongoDB
   * `Best Practice` is to mantain diff collection for diff type of Documents

---

# DataBase in MongoDB
* MongoDb Database is a group of Collection and
  * Collection are group of Documents
  * So MongoDb Database contains multiple Collection that i way contain multiple Documents
 ![image](https://user-images.githubusercontent.com/26667491/127466409-8196ecec-99ca-48b7-84a2-85f923c403af.png)
 
   * Quite Similar to database in RDBMS
 * Each instance of MondoDB Server can host multiple DB's
 * Bydefault there are `3 instances in every mongoDb, instances named as
   * `Admin, Local, Config`
   * Admin is root Db => any user having acess to this DB has acess to all DB's or resources in whole cluster

  ## `Naming Database`
   * Any alphanumeric character
   * Case-senstive
`_id field is a primary in MongoDb that uniquely identifies Document in a Collection`

![image](https://user-images.githubusercontent.com/26667491/127468344-b831aec8-a1e7-4c80-acea-3223a0b89a9d.png)

![image](https://user-images.githubusercontent.com/26667491/127468434-6c60086d-aa61-40c2-88fa-618dfcb45dc3.png)

`This is how a BSON document would encode a JSON document` 
 * Binary Encoded form of JSON
![image](https://user-images.githubusercontent.com/26667491/127468741-1043d215-85e5-44e8-8a28-979b6014876c.png)
   * Encodes `Length`, `Data type`, `Field name`, `Value represented by field`

![image](https://user-images.githubusercontent.com/26667491/127469396-ee5ae24f-9ec1-4a57-950c-dfc313618ae6.png)

* ('BSON Documentation')[https://bsonspec.org]
* ("BSON data type")[https://docs.mongodb.com/manual/reference/bson-types/#bson-types]
* ("MongoDB Storage")[https://www.mongodb.com/json-and-bson]

---
---

# About `mongod`
* Allows to make connection b/w MongoDB and Client
* to stablish this connection we nead to start mongod process on MongoDB host system 
  * mongod => is primary daemon process of MongoDb
  * daemon => process that runns in background
* mongod handles all data requests, manages data acess, perform background management operations
* mongod is present on every MongoDb server
![image](https://user-images.githubusercontent.com/26667491/127472098-77c1ec53-5bb3-4c28-b73a-b22384cb9dd3.png)

* ![image](https://user-images.githubusercontent.com/26667491/127472194-bb09ce3e-2bfe-4031-aa08-864a097cb937.png)
* mongod can be acessed using diff mongod clints like 
  * mongod shell
  * MongoDB Compas


![image](https://user-images.githubusercontent.com/26667491/127476598-d0e5f13b-31a3-4556-b047-5d3f22e0901b.png)
* (MongoDB Atlas)[https://www.mongodb.com/cloud/atlas]


