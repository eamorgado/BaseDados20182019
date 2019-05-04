import mysql.connector as msq
from prettytable import PrettyTable

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
        if self.database is not None:
            print("Already Connected to "+self.database)
            return self.mydb
        if self.findDataBase(db):
            ndb = DataBase(self.host,self.user,self.passw,db)
            ndb.getCursor()
            print("...Connected to "+db+"...")
            self.cursor = None
            self.getCursor()
            return ndb
        else:
            print("Database "+db+" does not exist")
            return self.mydb
    def getCursor(self):
        #Creates the cursor
        if self.cursor is None:
            self.cursor = self.mydb.cursor()
        return self.cursor
    def commit(self):
        self.mydb.commit()
    def execute(self,command,many=False,data=None):
        #execute command
        if many:
            self.cursor.executemany(command,data)
        else:
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
        else:
            print("Database "+db+" doesn't exist") 
    def printCursor(self,l=None):
        values = self.cursor.fetchall()
        if l is  not None:
            t = PrettyTable()
            t.field_names = l
            for val in values:
                t.add_row(val)
            print(t)
        else:
            for val in values:
                s = ""
                for x in val:
                    s += "{: >20}".format(str(x))+"\t"
                print(s)