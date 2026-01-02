import re
from logic import *
import numpy as np
parsing=False
fileFind=input("what is the name of the file you want")
file = open(fileFind+".fbb", "r")
content = file.read()
file.close()
tokens = re.findall(r"1|0",content)
tokensArray=np.array(tokens, dtype=int)
print(tokensArray)
parsing=True
iZero=0
iOne=1
iTwo=2
iThree=3
while parsing:
    binary(tokensArray[iZero],tokensArray[iOne],tokensArray[iTwo],tokensArray[iThree])
    print("working")
    iZero+=4
    iOne+=4
    iTwo+=4
    iThree+=4
    if iThree>tokensArray.size:
        break
    else:
        continue
