"""OOP in Python"""
"""4 method"""
#Imperative
Hadi_list = [1, 2, 3, 4, 5] 
sum = 0 
for x in Hadi_list:
    sum += x 
print(sum) 

#Procedural
def do_add(any_list): 
    sum = 0 
    for x in any_list: 
        sum += x 
    return sum 
print(do_add(Hadi_list)) 

#Functional
import functools
def add_it(x, y): 
    return (x + y) 
sum = functools.reduce(add_it, Hadi_list) 
print(sum) 

#Object Oriented
class ChangeList(object): 
    def __init__(self, any_list): 
        self.any_list = any_list 
    def do_add(self): 
        self.sum = sum(self.any_list) 
create_sum = ChangeList(Hadi_list) 
create_sum.do_add() 
print(create_sum.sum) 


"""---------------------------------------"""
class Person:
    def __init__(self, first_name, code_meli, age, gender):
        self.first_name=first_name
        self.code_meli=code_meli
        self.age=age
        self.gender=gender
    def get_code_melli(self):
        print(self.code_meli)    


person_1 = Person('Hadi', 13232, 25, 'male')
person_2 = Person('Amir', 13532, 20, 'male')

person_1.get_code_melli()
print(person_1.age)
print(person_2.first_name)
"""---------------------------------------"""
class Sample:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        
    def __call__(self, x, y):
        self.x=x
        self.y=y
    def Total_value(self):
        return self.x+self.y+self.z
Sample.z=3    
b = Sample(11, 12)
print(b.Total_value())

v = Sample()
print("object is callabe:", callable(v))
print('oldest x value:', v.x)

v(10, 9)
print('newest x value:', v.x)
"""---------------------------------------"""
class mobile:
    
    def __init__(self, pro, ram, dorbin, hard):
        self.pro=pro
        self.ram= ram
        self.dorbin=dorbin
        self.hard=hard
        
    def rate(self):
        return self.pro+ self.ram+ self.dorbin+ self.hard
    
mobile_sony=mobile(8, 12, 20, 64)
print(mobile_sony.rate())

class tablet(mobile):
    
    def rate(self):
        return self.pro+ self.ram+ self.dorbin+ self.hard+ self.lcd
    
tablet1=tablet(12, 12, 8, 64)
tablet1.lcd=12
print(tablet1.rate())