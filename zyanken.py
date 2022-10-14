'''
Created on 2022/10/14

@author: t20cs010
'''

import random
from change import changeNum
from result import result

a = random.randint(0, 2)
b = random.randint(0, 2)

print("aの手：", end = "")
changeNum(a)
print(" v.s. bの手：", end = "")
changeNum(b)
print(" → ", end = "")
result(a, b)