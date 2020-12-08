import random
import string


length = int(input('Strand Length: '))
nucleotides ={'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
def randStr(length):
    template = "ATGC"
    tempList = []
    for i in range(length):
        tempList.append(random.choice("".join([template])))
    return "".join(tempList)
   
randomStrand = randStr(length)
print("This is the random DNA strand : " + randomStrand + "\n" + "This function randomly produces a DNA strand depending on the length inputed by the user.")
    
    #next entry
def dnaRep():
    nontempStrand = ""
    for x in randomStrand:
        for key, value in nucleotides.items():
            if x == key:
                nontempStrand += value
    return nontempStrand

print("This is the non template strand : " + dnaRep() + "\n" + "This function matches the nucleotides on the random strand with the appropriate complementary DNA nucleotides.")
    
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
print("This is the mRNA Strand : " + dnaTranscription() + "\n" + "This function matches the nucleotides on the random strand with the appropriate RNA nucleotides.")
    
    

    
