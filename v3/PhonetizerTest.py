from Phonetizer import Phonetizer
def main():
    data="ሮ"
    x=Phonetizer(data,[])
    y=x.unicodeExtract("በ")
    #z=x.isAmharicConsonant("ግ")
    t=x.changeToPhonem(["ይሰብ","ይሰብ","?","ይሰብ","ይሰብ","ይሰብችሁ","?"])
    #t=x.geminate("ይሰብችሁ")
    #t=x.wordProsody("ይሰብችሁ",4,3)
    #print(z)
    print(t)
main()
