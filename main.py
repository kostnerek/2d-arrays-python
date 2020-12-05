
from calculator import Calc #get class 'Calc' from 'calculator.py'
from arrayLib import Array
import random,time
"""
list  = [] -> list.append(data)
dict  = {} -> like php {"set"=1, "name"=2}, doesnt have append
set   = {} -> poor dict
tuple = () -> ???
"""

def getRandom(qty,maxVal):
    a=[]
    for i in range(qty):
        a.append(random.randrange(0,maxVal,1))
    return a

def clear():
    print('\033c')



width  = 150#int(input("width: "))
height = 20#int(input("height: "))


while True:
    
    histogram = Array(height,width,0)
    rands = getRandom(width,height)
    #print(rands)
    for x in range(width):
        if(rands[x]==0):rands[x]+=1
        for i in range(rands[x]):
            histogram.modify(height-1-i,x,1)
    print('\033c')
    histogram.printReplace(0,1,1,'|',0,' ') 
    #histogram.printArray(1,1)
    time.sleep(0.5)






