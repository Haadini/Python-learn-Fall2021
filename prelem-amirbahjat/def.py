#mesal avval def
def my_function():
  print("Hello")

my_function()
"""----------------------------------------------------------------"""
#mesal dovvom ba arguman
def my_function(name):
  print(name + " bachate??")

my_function("ali")
my_function("ahmad")
my_function("sarar")
"""-----------------------------------"""
#mesal sevom def ba do arguman
def my_function(name, bname):
  print(name + " " + bname)

my_function("ali", "ahmadi")

"""---------------------------------------"""
#mesal sevom ba se arguman
def my_function(child3, child2, child1):
  print("javone ine " + child3)

my_function(child1 = "ali", child2 = "sara", child3 = "saba")
"""----------------------------------------------------------------"""
#mesal chaharom vaqti k mikhaeem az function estefade nakonim
def my_function(n):
    pass
"""-----------------------------"""
#mesal function ba return va for
def my_function(x):
  return 10 * x

print(my_function(5))

"""---------------------------------"""
def my_function(food):
  for x in food:
    print(x)

fruits =  "apple"

my_function(fruits)

"""---------------------------------"""
#mesal akhar ba tabe bazgashti
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    #inja az 6 ta 0 mire va engar az 0 shoro karde
    print(result)
  else:
    result = 0
  return result

print("Results ")
tri_recursion(6)