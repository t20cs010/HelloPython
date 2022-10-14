'''
Created on 2022/10/14

@author: t20cs010
'''
def result(a,b):
    if a == 0 and b == 1 or a == 1 and b == 2 or a == 3 and b == 0:
        print("aの勝ち")
    elif a == 0 and b == 0 or a == 1 and b == 1 or a == 2 and b == 2:
        print("引き分け")
    else:
        print("bの勝ち")