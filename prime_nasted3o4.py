#adad avval zire 100
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) :
       print (i, " is prime")
   i = i + 1

print ("Good bye!")
"""----------------------------------------------------------------"""
#begire bbine aya avvale???

x = input()
x=int(x)
c=0
for i in range(1,x):
    if (x%i==0):
        c+=1
if (c==1):
    print("prime")

else:
    print("not prime")