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
    conn.close()
main()
