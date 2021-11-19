"""optimization with scipy and greedy"""
"""Greedy"""
#greedy alghorithem
#knapsack problem

class Item(object):
    
    def __init__(self, n, v, w):
        self.name=n
        self.value=v
        self.weight=w
    
    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        result="("+ self.name + "," + str(self.value) + "," + str(self.weight) + ")"
        return result
        
def value(item):
    return item.getValue()

def weightinverse(item):
    return 1/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def OurItems():
    names = ["GAZ" , "GHAZA" , "GHORI", "CHAKME"]
    values = [9, 20, 10, 3]
    weights =[3, 5, 2, 1]
    Items = []
 
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

def greedy(items, maxWeight, keyFunction):
    sortedItems= sorted(items, key=keyFunction , reverse=True)
    result=[]
    totalValue=0
    totalWeight=0
    
    for i in range(len(sortedItems)):
        if (totalWeight+ sortedItems[i].getWeight()) <= maxWeight:
            result.append(sortedItems[i])
            totalWeight += sortedItems[i].getWeight()
            totalValue += sortedItems[i].getValue()
    return (result , totalValue)

def greedy1(items, constraint, keyFunction):
    res , val = greedy(items, constraint, keyFunction)
    print ("total value is: ",val)
    for item in res:
        print (" ", item)

def greedy2(maxWeight=5):
    items = OurItems()
    print("agar ba value pish beravim", maxWeight)
    greedy1(items, maxWeight, value)
    print("agar ba weight pish beravim", maxWeight)
    greedy1(items, maxWeight, weightinverse)
    print("agar ba nesbat pish beravim", maxWeight)
    greedy1(items, maxWeight, density)

print(greedy2(maxWeight=5))

"""--------------------------------------------------------------------------------------------"""
"""Fibonachi Dynami programming and Divide"""
def fDYNa(n, space={}):
    if n==1 or n==0:
        return 1
    try:
        return space[n]
    except KeyError:
        result = fDYNa(n-1, space) + fDYNa(n-2, space)
        space[n]=result 
        return result
"""-------------------"""
def dynamicFibo(n,table = []):
    while len(table) < n+1: 
        table.append(0)
      
           
    if n <= 1:       
        return n   
    else:       
        
        if table[n-1] ==  0:           
            table[n-1] = dynamicFibo(n-1)       
        if table[n-2] ==  0:   
            table[n-2] = dynamicFibo(n-2)    
        table[n] = table[n-2] + table[n-1]
    return table[n]
"""--------------------------------------------------------------------------------------------"""
"""scipy"""
# function object
#P+S+A+N
#s.t:
# P + S + A + N = 700
# A -0.5N = 0
# P + S <= 450
# S + N <= 300
# -P + S + A -N <= 0

from scipy.optimize import linprog

var_list=['porteghal','sib','anar','narengi']

c=[1,1,1,1]

A_eq=[[1, 1, 1, 1],
      [0, 0, 1, -0.5]]

A_ineq=[[1, 1, 0, 0],
        [0, 1, 0, 1],
        [-1, 1, 1, -1]]

B_eq=[700, 0]
b_ineq=[450, 300, 0]

Kharid_mive=linprog(c, A_ub=A_ineq, b_ub=b_ineq, A_eq=A_eq, b_eq=B_eq, method='interior-point')
print(Kharid_mive)