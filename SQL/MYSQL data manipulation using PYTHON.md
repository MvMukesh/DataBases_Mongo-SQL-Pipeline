# Manipulating MYSQL data using Python
---
`Cover`
![image](https://user-images.githubusercontent.com/26667491/127143749-f77d54fc-898f-4a06-ad30-d40ee4dd6127.png)

`Setting up a Virtual Env`
* pip install virtualenv
* `mkdir name`
* `cd name`
* `virtualenv project_name` (require internet)
  * Lib(directory): Contains the python version copy and site-packages directory where each dependency is installed.
project_name
├── bin <br>
├── lib
* `source project_name/bin/activate` => activate virtual env   => (venv) (base)
* `deactivate` => deactivate virtual env

`Installing Required Packages` 
* `pip install mysql-connector`  (library to connect MYSQL-SQL) other optional library can be Python-MYSQL, MYSQL-Client

`Coonecting ot MYSQL using mysql-connector`
* mysql_connection.py file
   * db = mysql.connector.connect(host ="127.0.0.1", port ="3306", user ='root',passwd ="12345",database ="fifa19")

`Connecting to database table and pulling data`
* mycursor =db.cursor()
* mycursor.execute("select * from players limit 1")
* ![image](https://user-images.githubusercontent.com/26667491/127153910-df228d53-117a-49ca-8b48-02fe4987b4ef.png)
  * Returns list of tuples here 1 tuple list
  * Each tuple will show 1 row obove we have only 1 row

`Querying database- INSERT,DELETE,SEARCH,INDEXING` => Python to MYSQL table
* all is in mysql_connection.py which is inside name folder

