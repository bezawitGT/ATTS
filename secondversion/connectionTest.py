from ConnectToDB import ConnectToDB
from Synthesiser import Synthesiser
def main():
    passw=""
    username="root"
    db="python_db"
    #creat connecton obj
    conn=ConnectToDB(username,passw,db,"")
    #connect to DB
    connection=conn.connect()
    #creat synthesiser obj
    syn=Synthesiser(connection,passw)
    #load sound using the load sound methond in synthesiser class
    loadSound=syn.loadSound([1])
    # print(y.get_server_info())
    #close connection
    conn.close()
main()
