import random
import string

def randStr(length):
    template = "ATGC"
    tempList = []
    for i in range(length):
        tempList.append(random.choice("".join([template])))
        
    return "".join(tempList)

length = int(input('Strand Length: '))
print(randStr(length))

#next entry
randStr = "ATTCGG"
nucleotides ={'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
def dnaRep():
    nontempStrand = ""
    for x in randStr:
        for key, value in nucleotides.items():
            if x == key:
                nontempStrand += value
    return nontempStrand
print(dnaRep())
