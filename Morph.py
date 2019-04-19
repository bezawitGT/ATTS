import l3
#l3.anal('am', 'ያስፈልግሻል')
class SemanticExtract:
    def __init__(self,subject,object,root,gender,plurality):
        self.__subject=subject
        self.__object=object
        self.__root=root
        self.__gender=gender
        self.__plurality=plurality
    def semanticExtract(self,tokenizedWords):
        j=''
        for i in tokenizedWords:
            x=str(l3.anal('am',i,roman=False, root=False, gram=False, citation=True, raw=False))
#            j=str(x)+"  "
#           y=x.rfind("stem")# or y=x.rfind("citation")
        return x
    
