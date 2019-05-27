import os
import wave
import nltk
from Tokeniz import Tokeniz
from ContextualAnalyzer import ContextualAnalyzer
from ConnectToDB import ConnectToDB
from Phonetizer import Phonetizer
from Synthesiser import Synthesiser
class AmharicTTS:
    def __init__(self,tokens,contextWords,phones,conn,synthesiser):
        self.tokens=tokens
        self.contextAnalyzedWords=contextWords
        self.phonems=phones
        self.connection=conn
        self.synthesiser=synthesiser
    #load sound from db
    def check(self,i):
        data=os.path.dirname(__file__) + "\\data\\1-100.txt"
        datafile = open(data,encoding="utf8")
        found = False
        for line in datafile:
            if i in line:
                found = True
                break
        return found
    def syntesis(self,word,mode):
        self.tokens=Tokeniz(word,[])
        tokens=self.tokens.tokenize()
        self.contextAnalyzedWords=ContextualAnalyzer(tokens,[])
        contexts=self.contextAnalyzedWords.contextuallyAnalyze()
        if mode==1:
            self.phonems=Phonetizer(contexts,[])
            phonem=self.phonems.changeToPhonem(contexts)
        #print(phonem)
            conn=ConnectToDB("root","","python_db","")
            self.connection=conn.connect()
            self.synthesiser=Synthesiser(self.connection,"")
            loadSound=self.synthesiser.loadSound(phonem)
        else:

            VOICE_PATH = os.path.dirname(__file__) + "\\data\\"
            OUTPUT_FILE = "output.wav"
            word=""
            #word=["አንድ","ገና","የዕድሮች","ደግሞ","ነገር","ውስጥ","ሰው","ቤት","ነው","ሥራ","ላይ"]
            #word=open(VOICE_PATH+"1-100.txt").read()
            infiles = []
            for i in contexts:
                if self.check(i) is True:
                    phone=VOICE_PATH + i + ".wav"
                    infiles.append(phone)
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
        return print("Speech Generated")
