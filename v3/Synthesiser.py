import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error
import wave, os
class Synthesiser:
    def __init__(self,conn,soundSequence):
        self.conn=conn
        self.soundSequence=soundSequence
    #load sound from db
    def loadSound(self,phonems):
        #set path for the sound
        VOICE_PATH = os.path.dirname(__file__) + "\\data\\"
        OUTPUT_FILE = "output.wav"
        infiles = []
        try:

            for phonem in phonems:
                sql_fetch_query = ("SELECT value from atts where name= %s")
                val=((phonem),)
                cursor = self.conn.cursor()
                cursor.execute(sql_fetch_query,val)
                record=cursor.fetchall()
                for row in record:
                    p=str(row[0])
                    phone=VOICE_PATH + p + ".wav"
                    #print(phone)
                    infiles.append(phone)
                #print("infiles: "+str(infiles))
            data = []
            for infile in infiles:
                w = wave.open(infile, 'rb')
                data.append( [w.getparams(), w.readframes(w.getnframes())] )
                w.close()
            #print("w: "+str(w))
            output = wave.open(OUTPUT_FILE, 'wb')
            output.setparams(data[0][0])
            len=infiles.__len__()
            count=0
            while len>0:
                output.writeframes(data[count][1])
                count +=1
                len -=1
            output.close()
        except mysql.connector.Error as error :
            self.conn.rollback()
            print("Failed to read data from MySQL table {}".format(error))
        return print("sucessful")
