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
