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
                if word[nex] in ["i","I"]:
                    wordUnicode.append(str(self.unicodeExtract(i))+word[nex])
                else:
                    wordUnicode.append(str(self.unicodeExtract(i)))
        return wordUnicode
    def nth_index(self,iterable,value,n):
        matches=(idx for idx,val in enumerate(iterable) if val==value)
        return next(islice(matches,n-1,n),None)
