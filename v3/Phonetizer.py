import nltk
import nltk.tokenize
from itertools import islice
class Phonetizer:
    def __init__(self,phonemes,unicodes):
        self.phonemes=phonemes
        self.unicodes=unicodes
    #extract the ASCII of a character
    def unicodeExtract(self,text):
        ASCII=ord(text)
        return ASCII
    #check if a character is amharic consonat or not
    def isAmharicConsonant(self,fidel):
        amharicConsonants=["ብ","ድ","ጅ","ፍ","ግ","ህ","ኅ","ሕ","ኽ","ይ","ክ","ቅ","ል","ም","ን","ኝ","ፕ","ጵ","ር","ስ","ሥ","ሽ","ት","ጽ","ፅ","ች","ጭ","ጥ","ቭ","ው","ዝ","ዥ","እ","ዕ"]
        if fidel in amharicConsonants:
            consonant=True
        else:
            consonant=False
        return consonant
    def geminate(self,word):
        charArray=list(word)
        i=0
        lengt=charArray.__len__()
        #print(lengt)
        while lengt>0:
            if self.isAmharicConsonant(charArray[i]):
                pos=i
                #print(pos)
                if pos==0:
                    charArray[i] = charArray[i]+"i"
                if pos == charArray.__len__()-1:
                    charArray[i] = charArray[i]
                if pos==1 and (charArray.__len__()-2) == pos:
                    charArray[i] = charArray[i]+"i"
                fina=(charArray[charArray.__len__()-1])
                if pos == (charArray.__len__()-2) and self.isAmharicConsonant(fina):
                    if self.sonorityCheck(charArray[-2],charArray[-1]) is True:
                        charArray[i]=charArray[i]+"i"
            i += 1
            lengt -= 1
        gword=""
        for i in charArray:
            gword+=i
        return gword
    def sonorityCheck(self,pen,final):
        sonorityLevel={"ብ":1,"ድ":1,"ጅ":1,"ግ":1,"ት":2,"ች":2,"ኽ":2,"ፕ": 2,"ቅ": 3,"ፕ": 3,"ጭ": 3, "ጵ": 3, "ዝ": 4,"ዥ": 4
                       ,"ህ":5,"ኅ":5,"ሕ":5,"ኽ":5,"ስ":5,"ሥ":5,"ሽ":5,"ፍ":5,"ጽ":6,"ፅ":6,"ም":7,"ን":7,"ንi":7,"ኝ":7,"ል":8,"ር":8,"ው":9,"ይ":9}
        sonor=True
        if(sonorityLevel[pen]>sonorityLevel[final]):
            sonor=False
        return sonor
    def wordProsody(self,finalChar,finalIndex,penInd):
        suffixes="ን ኝ ሽ ት ው ክ ህ ሁ ኩ ች ሽኝ ችኝ ከን ሽን ችን ኩህ ኩሽ ችሁ ችህ ንህ ችሽ ንሽ ኳት ነው ኋት ቻት ኩት ሻት ናት ቸው ኧኝ ከኝ ኩኝ ሁኝ ኧን ውህ ሁሽ ሁት ሁህ ለት በት ላት ባት ብህ ልህ ልሽ ብሽ ልኝ ብኝ ልን ብን ካት ከው ችሁኝ ኳችሁ ችሁን ናችሁ ቻችሁ ኳቸው ሻቸው ናቸው ቻቸው ኋችሁ ኋቸው ላቸው ባቸው ላችሁ ባችሁ ችበት ችለት ችባት ችላት ችብህ ችልህ ችልሽ ችብሽ ችብኝ ችልኝ ችብን ችልን ክበት ህበት ክለት ህለት ህባት ህላት ክባት ክላት ክብኝ ህብኝ ክልኝ ህልኝ ክብን ህብን ክልን ህልን ሽበት ሽለት ሽባት ሽላት ሽብኝ ሽልኝ ሽብን ሽልን ኩበት ሁበት ኩለት ሁለት ኩባት ኩላት ሁላት ሁባት ኩብህ ሁልህ ኩብሽ ሁልሽ ሁብህ ኩልህ ኩልሽ ሁብሽ ንባት ንላት ንብህ ንልህ ንብሽ ንልሽ ንለት ንበት ችኋት ችሁት ካቸው ችኋቸው ችባቸው ችላቸው ችላችሁ ችባችሁ ክባቸው ክላቸው ህባቸው ህላቸው ሽላቸው ሽባቸው ኩላቸው ኩባቸው ኩባችሁ ሁላችሁ ሁባችሁ ኩላችሁ ችሁብኝ ችሁልኝ ችሁልን ችሁብን ችሁባት ችሁላት ችሁበት ችሁለት ንባችሁ ንላችሁ ንባቸው ንላቸው ችሁባቸው ችሁላቸው"
        suffList=token=nltk.word_tokenize(suffixes)
        end=False
        for i in suffList:
            if str(finalChar).endswith(i):
                end=True
                final=list(finalChar)
                final[penInd]=finalChar[penInd]+"I"
                finalChar=final
        if end is False:
            finalChar=finalChar+"I"
        prosody=""
        for i in finalChar:
            prosody+=i
        return prosody
    #graphem to phonem converter
    def changeToPhonem(self,words):
        gemeneted=""
        #extract gemenation for every word in the sentence
        for i in words:
            gem=self.geminate(i)
            gemeneted += str(gem)+" "
        gem=nltk.word_tokenize(gemeneted)
        count=gemeneted.count("?")
        #analyze prosody for introgattive sentences
        if "?" in gemeneted:
            while count>0:
                index=self.nth_index(gem,"?",count)
                introgative=gem[index-1]
                final=len(introgative)
                pro=self.wordProsody(introgative,final-1,final-2)
                gem[index-1]=pro
                gem.pop(index)
                count -=1
        word=""
        #convert tokenized word in to a sentence
        for i in gem:
            word +=i+" "
        wordUnicode=[]
        #convert the gementated with prosody words to unicode
        print(word)
        for i in word:
            if i not in ["i","I","?"]:
                ind=word.index(i)
                nex=ind+1
                if nex!=len(word):
                    if word[nex] in ["i","I"]:
                        wordUnicode.append(str(self.unicodeExtract(i))+word[nex])
                    else:
                        wordUnicode.append(str(self.unicodeExtract(i)))
        return wordUnicode
    def nth_index(self,iterable,value,n):
        matches=(idx for idx,val in enumerate(iterable) if val==value)
        return next(islice(matches,n-1,n),None)
