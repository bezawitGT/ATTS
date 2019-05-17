import nltk
import nltk.tokenize
class Tokeniz:
    #tokenizer constructor
    def __init__(self,words,tokenizedWords=[]):
        self.words=words
        self.tokenizedWords=tokenizedWords
     #translate row numbers in to writen out words
    def numberTranslat(self,token):
    #find numbers inside the tokenized word
        for i in token:
            if i.isnumeric() or i.isdigit():
                if len(i)<=5:# if the number is 5 digits or less find the approperate words p=position d=digit
                    count=0
                    l=len(i)-1
                    z=""#store the translated number
                    while count<len(i):
                        p=l
                        d=i[count]
                        count +=1
                        l=l-1
                        z=z+self.num(int(p),int(d))
#                print(z)
                elif len(i)>5:# for numbers with more that 5 digits find approperate words
                    count=0
                    z=""
                    while count<len(i):
                        d=i[count]
                        count +=1
                        z=z=z+self.nums(int(d))
#                print(z)
                x=token.index(i)
                token[x]=z
        return token
    def abbrivationTranslation(self,token):
        for i in token:
            if '/' in i or '.' in i:
                trans=self.abbrivSearch(i)
                x=token.index(i)
                token[x]=trans 
#            print(trans)
#print(nubTrans(token))
        return token
#search for abbrivations in the database
    def getTokens(self):
        return self.tokenizedWords
    def abbrivSearch(self,abbr):
        mostKnownAbbrivations="ዶ/ር አ/አ/ዩ ዓ/ም ጠ/ሚኒስትሩ ሚ/ር ፍ/ቤት ፍርድ ቤት ጽ/ቤት ም/ቤት ጠ/ሚኒስትር መ/ቤት ፕ/ር ኢ/ር ፅ/ቤት የዶ/ር መ/ቤቶች ጠ/ሚ ወ/ሪት መ/ቤቱ ገ/እግዚአብሔር ወ/ት ገ/ማርያም ገ/ሥላሴ ክ/ከተማ ኃ/ማርያም ኢዜአ/ ገ/ሕይወት ት/ቤቱ በ40/60 ገ/ስላሴ በ20/80 ወ/ጊዮርጊስ በወ/ሮ ቅ/ጊዮርጊስ ኃ/ሥላሴ ሊ/መንበር	ሚ/ሩ ሲ/ር ም/ፕሬዚዳንት ም/ሊቀመንበር ጠ/ሚ/ር	 ጽ/ቤቶች ወ/ሚካኤል ኤች.አይ.ቪ/ኤድስ ኪ/ሜትር ኃ/የተ/የግ/ማህበር ኃ/ጊዮርጊስ ም/ጠ/ሚኒስትር ም/ዋና ወ/ሥላሴ ኃ/ስላሴ 70/30 ኢዜአ/ መ/ቤቶች ቅ/ሲኖዶስ ክ/ሀገር ሌ/ኮሎኔል ተ/ሃይማኖት ዲ/ን በወ/መ/ሥ/ሥ/ሕ/ቁ ኤች.አይ.ቪ ሊ/መንበር ት/ክፍል አ/ማ ጠ/ፍ/ቤት የአይ.ኤ.ኤ.ኤፍ ብ.ኢ.ኮ ሲ.ቲ ሰ.ዐ.ወ አ.ኤ.አ የሲ.ኤን.ኤን ከአይ.ሲ.ቲ በእ.ኤ.አ	 እ.ኤአ የዲ.ኤስ.ቲቪ ሲ.አይ.ኤ እ.ኤ ኃ.የተ.የግ.ማህበር ፒ.ኤል.ሲ የኤፍ.ኤ አ.አ.ዩ ከኢ.ፌ.ዴ.ሪ	ተ.መ.ድ ሚ.ሜ እ.እ.እ ኢ.ሴ.ማ.ቅ"
        abbri={"አ.አ.ዩ":"አዲስ አበባ ዩኒቨርሲቲ","አ/አ/ዩ":"አዲስ አበባ ዩኒቨርሲቲ", "ዓ/ም":"ዓመተ ምህረት","ዶ/ር":"ዶክተር","ጠ/ሚኒስትሩ":"ጠቅላይ ሚኒስተር","ሚ/ር":"ሚኒስተር","ፍ/ቤት":"ፍርድ ቤት","ጽ/ቤት":"ጽፈት ቤት","ም/ቤት":"ምክር ቤት","ጠ/ሚኒስትር":"ጠቅላይ ሚኒስተር","መ/ቤት":"መስሪያ ቤት","ኢ/ር":"ኢንጂነር"	,"ፅ/ቤት":"ጽፈት ቤት","ጠ/ሚ":"ጠቅላይ ሚኒስተር","ወ/ሪት":"ወይዘሪት","ገ/እግዚአብሔር":"ገብረ እግዚአብሔር","ወ/ት":"ወይዘሪት","ገ/ማርያም":"ገብረ ማርያም","ገ/ሥላሴ":"ገብረ ሥላሴ","ክ/ከተማ":"ክፍለ ከተማ","ኃ/ማርያም":"ኃይለ ማርያም","ኢዜአ/":"ኢትዮጽያ ዜና አገልግሎት","ገ/ሕይወት":"ገብረ ሕይወት","40/60":"አርባ ስልሳ","ገ/ስላሴ":"ገብረ ስላሴ","በ20/80":"ሃያ ሰማንያ","ወ/ጊዮርጊስ":"ወልደ ጊዮርጊስ","ወ/ሮ":"ወይዘሮ","ቅ/ጊዮርጊስ":"ቅዱስ ጊዮርጊስ","ኃ/ሥላሴ":"ኃይለ ሥላሴ","ሊ/መንበር":"ሊቀ መንበር","ሲ/ር":"ሲስተር","ም/ፕሬዚዳንት":"ምክትል ፕሬዚዳንት","ም/ሊቀመንበር":"ምክትል ሊቀመንበር","ጠ/ሚ/ር":"ጠቅላይ ሚኒስተር","ወ/ሚካኤል":"ወልደ ሚካኤል","ኤች.አይ.ቪ/ኤድስ":"ኤችአይቪ ኤድስ","ኪ/ሜትር":"ኪሎ ሜትር","ኃ/የተ/የግ/ማህበር":"ኃላፊነቱ የተወሰነ የግል ማህበር","ኃ/ጊዮርጊስ":"ኃይለ ጊዮርጊስ","ም/ጠ/ሚኒስትር":"ምክትል ጠቅላይ ሚኒስተር","ወ/ሥላሴ":"ወልደ ሥላሴ","ኃ/ስላሴ":"ኃይለ ሥላሴ","70/30":"ሰባ ሰላሳ","ቅ/ሲኖዶስ":"ቅዱስ ሲኖዶስ","ክ/ሀገር":"ከፍለ ሀገር","ሌ/ኮሎኔል":"ሌተናል ኮሎኔል","ተ/ሃይማኖት":"ተክለ ሃይማኖት","ዲ/ን":"ዲያቆን","በወ/መ/ሥ/ሥ/ሕ/ቁ":"በወንጀል መቅጫ ህዝብ ቁጥር","ኤች.አይ.ቪ":"ኤችአይቪ","ሊ/መንበር":"ሊቀ መንበር","አ/ማ":"አክስዮን ማህበር","ጠ/ፍ/ቤት":"ጠቅላይ ፍርድ ቤት","የሲ.ኤን.ኤን":"የሲኤንኤን","አይ.ሲ.ቲ":"አይሲቲ","እ.ኤአ":"እንደ ኤውሮፓያን አቆጣጠር","ዲ.ኤስ.ቲቪ":"ዲኤስቲቪ","ሲ.አይ.ኤ":"ሲአይኤ","ፒ.ኤል.ሲ":"ፒኤልሲ","የኤፍ.ኤ":"የኤፍኤ","አ.አ.ዩ":"አዲስ አበባ ዩንቨርስቲ","ከኢ.ፌ.ዴ.ሪ":"ኤፌድሪ","ተ.መ.ድ":"የተባበሩት መንግስታት ድርጅት","ሚ.ሜ":"ሚሊ ሜትር","እ.እ.እ":"ኢትዮጽያ ዜና አገልግሎት"}
        if abbr in mostKnownAbbrivations:
            r=abbri[abbr]
        elif '/' in abbr:
            r=abbr.replace("/", " ")
        elif '.' in abbr:
            r=abbr.replace(".", "ነጣ ")
        return r
    def nums(self,d):
        r=""
        if d==0:
            r="ዜሮ "
        elif d==1:
            r="አንድ "
        elif d==2:
            r="ሁለት "
        elif d==3:
            r="ሶስት "
        elif d==4:
            r="አራት "
        elif d==5:
            r="አምስት "
        elif d==6:
            r="ስድስት "
        elif d==7:
            r="ሰባት "
        elif d==8:
            r="ስምንት "
        elif d==9:
            r="ዘጠኝ "
        return r
    #function to translitate numbers with less than 5 digits the position of the numbers is also necessary
    def num(self,p,d):
        r=""
        if p==0 and d==1:
            r="አንድ "
        elif p==1 and d==1:
            r="አስራ "
        elif p==2 and d==1:
            r="አንድ መቶ "
        elif p==3 and d==1:
            r="አንድ ሺ "
        elif p==4 and d==1:
            r="አስራ "
        elif p==0 and d==2:
            r="ሁለት "
        elif p==1 and d==2:
            r="ሃያ "
        elif p==2 and d==2:
            r="ሁለት መቶ "
        elif p==3 and d==2:
            r="ሁለት ሺ "
        elif p==4 and d==2:
            r="ሃያ "
        elif p==0 and d==3:
            r="ሶስት "
        elif p==1 and d==3:
            r="ሰላሳ "
        elif p==2 and d==3:
            r="ሶስት መቶ "
        elif p==3 and d==3:
            r="ሶስት ሺ "
        elif p==4 and d==3:
            r="ሰላሳ "
        elif p==0 and d==4:
            r="አራት "
        elif p==1 and d==4:
            r="አርባ "
        elif p==2 and d==4:
            r="አራት መቶ "
        elif p==3 and d==4:
            r="አራት ሺ "
        elif p==4 and d==4:
            r="አርባ "
        elif p==0 and d==5:
            r="አምስት "
        elif p==1 and d==5:
            r="ሃምሳ "
        elif p==2 and d==5:
            r="አምስት መቶ "
        elif p==3 and d==5:
            r="አምስት ሺ "
        elif p==4 and d==5:
            r="ሃምሳ "
        elif p==0 and d==6:
            r="ስድስት "
        elif p==1 and d==6:
            r="ስልሳ "
        elif p==2 and d==6:
            r="ስድስት መቶ "
        elif p==3 and d==6:
            r="ስድስት ሺ "
        elif p==4 and d==6:
            r="ስልሳ "
        elif p==0 and d==7:
            r="ሰባት "
        elif p==1 and d==7:
            r="ሰባ "
        elif p==2 and d==7:
            r="ሰባት መቶ "
        elif p==3 and d==7:
            r="ሰባት ሺ "
        elif p==4 and d==7:
            r="ሰባ "
        elif p==0 and d==8:
            r="ስምንት "
        elif p==1 and d==8:
            r="ሰማንያ "
        elif p==2 and d==8:
            r="ስምንት መቶ "
        elif p==3 and d==8:
            r="ስምንት ሺ "
        elif p==4 and d==8:
            r="ሰማንያ "
        elif p==0 and d==9:
            r="ዘጠኝ "
        elif p==1 and d==9:
            r="ዘጠና "
        elif p==2 and d==9:
            r="ዘጠኝ መቶ "
        elif p==3 and d==9:
            r="ዘጠኝ ሺ "
        elif p==4 and d==9:
            r="ዘጠና "
        elif p==1 and d==0:
            r="መቶ "
        elif p==2 and d==0:
            r="ሺ "
        elif p==3 and d==0:
            r="ሺ "
        return r
# tokenizer function which perform word tokenization, and number/abbriv translation
    def tokenize(self):
        token=nltk.word_tokenize(self.words)
        t=self.numberTranslat(self.abbrivationTranslation(token))
        #print(t)
        word=""
        for i in t:
            word +=i+" "
        self.tokenizedWords=nltk.word_tokenize(word)
        return self.tokenizedWords
   # print(tokenize(data))
    #tokenizedWords=tokenize(data)
