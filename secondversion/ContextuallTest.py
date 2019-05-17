import nltk
import nltk.tokenize
from ContextualAnalyzer import ContextualAnalyzer
def main():
    data="ገና ነው ገና በአል የዕድሮች ጉድ አለ"
    tok=nltk.word_tokenize(data)
    z=ContextualAnalyzer([],tok)
    print(z.contextuallyAnalyze())
main()
