import mysql.connector as msq

class DataBase():
    def __init__(self,given_host,given_user,given_pass,given_database=None):
        #The initiating class, given a host, user and user pass, opens a conn
        self.host = given_host
        self.user = given_user
        self.passw = given_pass
        self.database = given_database
        if given_database is not None:
            self.mydb = msq.connect(
                host = str(given_host),
                user = str(given_user),
                passwd = str(given_pass),
                database = str(given_database)
                
            )
        else:
            self.mydb = msq.connect(
            host = str(given_host),
            user = str(given_user),
            passwd = str(given_pass)
        )
        self.cursor = None
        
    def connectTo(self,db):
        if self.findDataBase(db):
            ndb = DataBase(self.host,self.user,self.passw,db)
            ndb.getCursor()
            print("...Connected...")
            return ndb
        else:
            print("Database "+db+" does not exist")
            return self.mydb
    def getCursor(self):
        #Creates the cursor
        if self.cursor is None:
            self.cursor = self.mydb.cursor()
        return self.cursor
    def execute(self,command):
        #execute command
        self.cursor.execute(command)
    def showDatabases(self,p=False):
        #executes SHOW DATABASES if p=True prints result
        self.execute("SHOW DATABASES")
        if p:
            print("Databases:")
            for db in self.cursor:
                print("\t"+db[0])
    def findDataBase(self,db):
        #Searches all databases to see if db exists
        self.showDatabases()
        for d in self.cursor:
            if d[0] == db:
                return True
        return False
    def makeDataBase(self,db):
        if not self.findDataBase(db): 
            self.execute("CREATE DATABASE "+db)
        else:
            print("Database "+db+" already exisits")
    def deleteDataBase(self,db):
        if self.findDataBase(db):
            cmd = "DROP DATABASE %s",db
            self.execute("DROP DATABASE "+db) 