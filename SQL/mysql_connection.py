import mysql.connector
from pprint import pprint

try:
    # connecting mysql to python
    db = mysql.connector.connect(host ="127.0.0.1", port ="3306", user ='root',
                                 passwd ="12345", database ="fifa19")

    ## Connecting to database table and pulling data
    mycursor =db.cursor()
    #mycursor.execute("select * from players limit 2")
    #result =mycursor.fetchall()  # return output of select function to python
    #pprint(result)

    ## Querying the database- Create table inside fifa19 db  => 1
    #mycursor.execute("create table Contacts (Name varchar(255), PhoneNumber int(12))")

    ## INSERT values in Contacts table  => 2
    cmd = "insert into Contacts (Name ,PhoneNumber) values (%s ,%s)"
    val = ("Minue", 8994)

    mycursor.execute(cmd,val)

    db.commit()   # to make sure it commits perfectly

except Error as error:
    print(eroor)

finally:
    mycursor.close()
    db.close()


