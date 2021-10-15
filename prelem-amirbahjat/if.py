#mesal avval faghat form if
a = 30
b = 100

if b > a:
  print("b bozorgtar a")

"""------------------------"""
#mesal dovvom elif
a = 55

b = 99
if b > a:
  print("b bozorgtar a")
elif a == b:
  print("a o b mosavian")

"""------------------------"""
#mesal sevvom else
a = 200
b = 33
if b > a:
  print("b bozorgtar a")
elif a == b:
  print("a o b mosavian")
else:
  print("a bozorge?? b")

"""------------------------"""
#mesal chaharrom if short
a = 500
b = 1

if a > b: print("a bozorgtar b")

"""--------------------------"""
#mesal panjom short if else
a = 2
b = 800

print("A") if a > b else print("B")

"""---------------------------"""
#mesal if va and
a = 1000
b = 55
c = 666
if a > b and c > a:
  print("Both are True")

"""--------------------------"""
#mesal OR va if
a = 222
b = 33
c = 444
if a > b or a > c:
  print("yekish True")
