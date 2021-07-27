# Indexing
* For fast queries and search
![image](https://user-images.githubusercontent.com/26667491/127133120-0a76b630-d1db-4949-a147-7a46648d7903.png)
* `Tradeoff` increased insert/update time, improved search time 
----
`Cover`
![image](https://user-images.githubusercontent.com/26667491/127132698-f392f7b2-9cef-47e9-b9db-ceade80ed495.png)

![image](https://user-images.githubusercontent.com/26667491/127133892-ea63b2f6-6963-4ff9-bc0a-b1ff61efdefa.png)
* to perform same thing on number it requires complex data structure like b-tree
* `Downside of indexing`
  *  when new book comes, we nead to place book in particular place and find old book and replace with new
  *  So insert and update booth takes some time to execute
  *  Link [b-tree](https://www.codespeedy.com/how-to-implement-binary-tree-in-python/)

### `Relationships`

![image](https://user-images.githubusercontent.com/26667491/127117631-e2848c5f-11db-4d59-81c1-8b84780b8642.png) ![image](https://user-images.githubusercontent.com/26667491/127117893-4a09d8be-aee0-4e16-bfb1-240599748127.png)
* id_user, id_job have relationship with two tables user and job table

 ### `Types of Relationships`
* ![image](https://user-images.githubusercontent.com/26667491/127135895-4909d694-b498-484a-a293-de414737f5e1.png)

### `Table Constraints`
* Puts constraints on data inserted in table, violating data constraints is not allowed in MYSQL

### `Types of Constraints`
* ![image](https://user-images.githubusercontent.com/26667491/127136857-84b963c7-ac86-4abb-a591-92cacbc29e57.png)
* `Primary key`
  * In a table only one primary key is possible (one column of table can be a primary key )
  * used to identify rows, so it must be unique
  * `used to model one-to-one relationship`
* `Foreign key`
  * Example: user_id field in applied table is foreign key, of, user_id field of user detail table
  * Reason is we want user of only user_detail table to apply
  * `used ot model one-to-many relationship`
