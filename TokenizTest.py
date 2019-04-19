from Tokeniz import Tokeniz
def main():
    data="ሮበርትስ ዶ/ር ሰውነቱና አ/አ/ዩ ማጤንም ያስፈልግሻል? የዕድሮች ዓ/ም 5641 አ.አ.ዩ  990 የሞሪንጋ 679890 ካወጁ በተመዘገቡ"
    x=Tokeniz(data,[])
    x.tokenize()
    print(x.getTokens())
main()
