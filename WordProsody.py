
class WordProsody:
    
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

