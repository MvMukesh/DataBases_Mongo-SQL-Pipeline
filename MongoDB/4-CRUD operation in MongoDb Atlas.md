# CRUD operation Using ATLAS

(Atlas)[https://cloud.mongodb.com]
Action | How
---- | ----
Create a db user | ![image](https://user-images.githubusercontent.com/26667491/127851562-9deee13b-7b66-4d32-b061-1e86d9de6ce0.png)
Provide acess to it |  ![image](https://user-images.githubusercontent.com/26667491/127851591-cbc4c0a5-2415-49e0-a4e5-0cb6900228a1.png)
Load sample dataset on Atlas Cluster | ![image](https://user-images.githubusercontent.com/26667491/127851724-b2a357ef-d7de-447e-82ac-e261b636238d.png)
connection mongo shell to atlas cluster | [/users/mvon/mongodb/bin/mongo "mongodb+srv://cluster0.p5yk0.mongodb.net/myFirstDatabase" --username user_1]
Import,Export in atlas | ![image](https://user-images.githubusercontent.com/26667491/127854607-e8035a5a-a5d3-4c27-b35d-2e33cf84c40d.png)![image](https://user-images.githubusercontent.com/26667491/127854718-395af02e-60a0-48dd-872a-e71a6bf7354b.png)
Export from atlas | /Users/mvon/mongodb/bin/mongodump --uri mongodb+srv://user_1:@cluster0.p5yk0.mongodb.net --out /Users/mvon/Desktop/AV/W37-MongoDB/Atlas_sample_Data
Restore these Export to local mongodb server | mongorestore /path of directory (no connect to local mongodb server by using mongo shell as show dbs will see all dbs now here) [working on Atlas server is advised as this is what is required in real time] 

