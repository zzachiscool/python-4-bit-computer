#gets a file with .fbb at the end
import re
from logic import *
import numpy as np
fileFind=input("what is the name of the file you need(dont say the extention)")
file = open(fileFind+".fbb", "r")
content = file.read()
print(content)
file.close()
tokens = re.findall(r"1|0",content)
tokensArray=np.array(tokens, dtype=int)
print(tokensArray)
binary(tokensArray[0],tokensArray[1],tokensArray[2],tokensArray[3])