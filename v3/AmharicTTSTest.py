from Tokeniz import Tokeniz
from AmharicTTS import AmharicTTS
def main():
        wor="ሥራ ላይ ነገር ነው  "
        #wor="   ቤት ውስጥ ደግሞ አንድ ነገር ነው ነገር"
        tts=AmharicTTS("","","","","")
        print(tts.syntesis(wor,2))
main()
