import random
import string

class dnaTools:
    length = int(input('Strand Length: '))
    nucleotides ={'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    def randStr(length):
        template = "ATGC"
        tempList = []
        for i in range(length):
            tempList.append(random.choice("".join([template])))
        return "".join(tempList)
   
    randomStrand = randStr(length)
    
    #next entry
        def dnaRep():
        nontempStrand = ""
        for x in randomStrand:
            for key, value in nucleotides.items():
                if x == key:
                    nontempStrand += value
        return nontempStrand
    
    def dnaTranscription():
        mRNA = ""
        x = 0
        for x in randomStrand:
            if x == 'A':
                mRNA += 'U'
            else:
                for key, value in nucleotides.items():
                    if x == key:
                        mRNA += value
        return mRNA
print(dnaTools)
    
