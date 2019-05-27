import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error
class ConnectToDB:
    def __init__(self,userName,password,dbName,connection):
        self.userName=userName
        self.password=password
        self.dbName=dbName
        self.connection=connection
    #creat database connection
    def connect(self):
        try:
            connection = mysql.connector.connect(host='localhost',database=self.dbName,user=self.userName,password=self.password)
            if connection.is_connected():
                self.connection=connection
                #db_Info = connection.get_server_info()
                #print("Connected to MySQL database... MySQL Server version on ",db_Info)
        except Error as e :
            print ("Error while connecting to MySQL", e)
        return self.connection
    #close database connection
    def close(self):
        if(self.connection.is_connected()):
            #cursor = self.connection.cursor()
            #cursor.close()
            self.connection.close()
            closed=True
            print("MySQL connection is closed")
        else:
            closed=False
        return closed
