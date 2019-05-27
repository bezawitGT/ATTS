from Tokeniz import Tokeniz
def main():
    data="ሮበርትስ ዶ/ር ሰውነቱና አ/አ/ዩ ማጤንም ያስፈ/ልግሻል? 4.6 የዕድሮች ዓ/ም 5641 አ.አ.ዩ  990 የሞሪንጋ 679890 ካወጁ በተመዘገቡ"
    x=Tokeniz(data,[])
    x.tokenize()
    x.getTokens()
main()
#from Morph import SemanticExtract
#x=SemanticExtract(subject="",object="",root="",gender="",plurality="")
#x.semanticExtract(["ሮበርትስ","ዶ/ር","ሰውነቱና","ማጤንም"])
