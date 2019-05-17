import nltk
from itertools import islice
class ContextualAnalyzer:
    def __init__(self,analyzedWords,words):
        self.words=words
        self.analyzedWords=analyzedWords
    #analayze most frequent geninated words contextrullay
    def contextuallyAnalyze(self):
        #3 of most commenly happenning words
        geminatedWords=["አለ","ገና","ዋና","አለች"]
        #search wether geminated word exist in the sentes to be read for each word
        if geminatedWords[0] in self.words:
            HeSaidWeak={"ጉድ","አይደል","ምን"} # most likely occuring neighborhood words for አለ when it's not stressed "he said'
            count=self.words.count(geminatedWords[0])
            # add the meanining next to it for every words
            while count>0:
                word=self.words
                geminatedWordindex=self.nth_index(word,geminatedWords[0],count)
                beforGem=geminatedWordindex-1
                afterGem=geminatedWordindex+1
                if self.words[beforGem] in HeSaidWeak or self.words[afterGem] in HeSaidWeak:
                    self.words[geminatedWordindex]="አለsaid"
                count=count-1
        if geminatedWords[1] in self.words:
            xMas={"በአል","ልደት","29","ደረሰ ጫወታ"}
            count=self.words.count(geminatedWords[1])
            while count>0:
                word=self.words
                geminatedWordindex=self.nth_index(word,geminatedWords[1],count)
                beforGem=geminatedWordindex-1
                afterGem=geminatedWordindex+1
                if self.words[beforGem] in xMas or self.words[afterGem] in xMas:
                    self.words[geminatedWordindex]="ገናxmas"
                count=count-1
        if geminatedWords[2] in self.words:
            swim={"በአል","ዋኝን","ልንዋኝ","አስተማሪ","ተማሪ","ቦታ","ገንዳ","ልንሄድ","ሊሄዱ","ልሄድ","ሊሄድ","እችላለሁ","ይችላል","ትችላለች","አልወድም","አትወድም","አይወድም","አንወድም","አልችልም","አትችልም","አይችሉም","ዋኝን","ልንዋኝ","አስተማሪ","ተማሪ","ቦታ","ገንዳ","ልንሄድ","ሊሄዱ","ልሄድ","ሊሄድ","እችላለሁ","ይችላል","ትችላለች","አልወድም","አትወድም","አይወድም",
                  "አንወድም","አልችልም","አትችልም","አይችሉም"}
            count=self.words.count(geminatedWords[1])
            while count>0:
                word=self.words
                geminatedWordindex=self.nth_index(word,geminatedWords[2],count)
                beforGem=geminatedWordindex-1
                afterGem=geminatedWordindex+1
                if self.words[beforGem] in swim or self.words[afterGem] in swim:
                    self.words[geminatedWordindex]="ዋናswim"
                count=count-1
        self.analyzedWords=self.words
        return self.analyzedWords
                #if i in self.words:
    def nth_index(self,iterable,value,n):
        matches=(idx for idx,val in enumerate(iterable) if val==value)
        return next(islice(matches,n-1,n),None)
