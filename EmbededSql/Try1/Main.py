import DataBase as DB
from Data import data
from Data import movies

db = DB.DataBase("localhost","root","londres99")
cursor = db.getCursor()
if db.findDataBase("testdb"):
    db.deleteDataBase("testdb")
db.makeDataBase("testdb")
db = db.connectTo("testdb")
cursor = db.getCursor()

db.execute("DROP TABLE IF EXISTS USERS")
db.execute("CREATE TABLE USERS(UserId INTEGER AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(255),Age INTEGER(3),Email VARCHAR(255) DEFAULT NULL)")
db.execute("SHOW TABLES")
db.printCursor(["Tables"])
print

data_set = data()

cmd = "INSERT INTO USERS(Name,Age,Email) VALUES (%s, %s, %s)"
db.execute(cmd,True,data_set)
db.commit()

db.execute("SELECT * FROM USERS")
db.printCursor(["UserId","Name","Age","Email"])
print

db.execute("SELECT * FROM USERS WHERE Name like '%Smith%'")
db.printCursor(["UserId","Name","Age","Email"])
print

db.execute("DROP TABLE IF EXISTS MOVIE")
db.execute("CREATE TABLE MOVIES(MovieId INT(11) PRIMARY KEY,Title VARCHAR(255) NOT NULL,Year SMALLINT(6) NOT NULL,Duration SMALLINT(6) NOT NULL)")
db.execute("SHOW TABLES")
db.printCursor(["Tables"]) 

data_set = movies()
cmd = "INSERT INTO MOVIES(MovieId,Title,Year,Duration) VALUES(%s, %s, %s, %s)"
db.execute(cmd,True,data_set)
db.commit()

db.execute("SELECT * FROM MOVIES ORDER BY Year DESC LIMIT 10")
db.printCursor(["MovieId","Title","Year","Duration"])
