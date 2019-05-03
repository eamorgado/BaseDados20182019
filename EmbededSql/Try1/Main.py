import DataBase as DB

'''-----------------------------------------------------------------------------
Open database access
-----------------------------------------------------------------------------
mydb = msq.connect(
    host = "localhost",
    user = "root",
    passwd = 'londres99'
)


-----------------------------------------------------------------------------
Cursor - Executer of commands
-----------------------------------------------------------------------------
mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE testbd")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db[0])
'''
db = DB.DataBase("localhost","root","londres99","testdb")
cursor = db.getCursor()

db.showDatabases(True)
db.makeDataBase("testdb")

#db.execute("CREATE TABLE users (user_id INTEGER AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),age INTEGER(3),email VARCHAR(255) DEFAULT NULL)")
