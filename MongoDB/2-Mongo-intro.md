# Quick Intro to MongoDB

* MongoDB is NoSQL database, follows document based model, designed for ease of development & scalling
  * `Features:` Flexibility, High availability, Horizontal Scalability, Rich query 

---
![image](https://user-images.githubusercontent.com/26667491/127442274-650d3d9b-0f9e-466c-ae16-9407095b9d1f.png)
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
