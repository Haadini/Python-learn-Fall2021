#tozih list
thislist = ["koft :)", "dard", "kabab"]
print(thislist) #in ye liste
#mitone intory ham bshe ::
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#va bgim slicing ro anjam bde
print(thislist[:4])
print(thislist[:-4])
print(thislist[8:4])

####################################################
####################################################
#mitonim item list haro change konim
thislist = ["koft :)", "dard", "kabab"]
thislist[1] = "zahre mar =) "
print(thislist)
#ya bgim
thislist[1:2] = ["pizza", "sambose"]
print(thislist)
#khodeton tarkibesho bhm bznin

####################################################
####################################################
thislist = ["koft :)", "dard", "kabab"]
thislist.append("pizza") #ezafe mikone b tahesh
thislist.insert(1 , "pizza") #dar 1 qararesh mide
b = ["pizza" , "sambose"]
thislist.extend(b) #ye list ro michsbone besh

####################################################
####################################################
#anva e hazf
thislist = ["koft :)", "dard", "kabab"]
thislist.remove("dard")
thislist.pop(2)
del thislist[0]
print(thislist)

####################################################
####################################################
#loop dar list
thislist = ["koft :)", "dard", "kabab"]
for i in range(len(thislist)):
  print(thislist[i])

#### yaaaa ba while
thislist = ["koft :)", "dard", "kabab"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

####################################################
####################################################
#sort kardan
thislist = ["koft :)", "dard", "kabab"]
thislist.sort()#b tartib python
thislist.sort(reverse = True) #sort bar ax
print(thislist)

####################################################
####################################################
#copy  kardan
thislist = ["koft :)", "dard", "kabab"]
mylist = thislist.copy()
print(mylist)

####################################################
####################################################
#join do ya chand list b ham
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

####################################################
####################################################