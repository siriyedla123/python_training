import mysql.connector
db =mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="root",
     database="testdatabase"
     )
mycursor = db.cursor()
mycursor.execute("CREATE TABLE Event(Event_name text PRIMARY KEY,location text,Person text,Location text,Date date")
mycursor.execute("Describe Event")
for x in mycursor:
     print(x)           
