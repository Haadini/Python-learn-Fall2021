#string
#mesal khode string
a = "Hello"
b = """hello im 
amir
and
im very happy""" #ba seta qoute mishe chand satr nevesht
print(a)
print(a[2]) #shomare character ke az 0 shoro mishe
print(b)
for i in a : #ino joda goneh run konin :))))
    print(i)
#function len ham dashtim
print(len(a)) #tool a ro mohasebe mikard
#if b ma migof k agar folan kalame to motaghayer hast True false esh ro bhm bgo
if "amir" in b :
    print(True)
##############################################
##############################################
#baksh dovvom boresh ya slicing
b = "hello python nevis"
print(b[2:])
print(b[6:7])
print(b[-6:-7])
#in niaz b test dare khodeton benevisinsh


##############################################
##############################################
#bakhsh sevvom method haye mohm
x = "hello world   "
print(x.strip())#space ro hazf mikone
print(x.lower())#horofo kochik
print(x.upper())#horofo bozorg mikone
print(x.replace("h" , "H"))#jabeja mikone

##############################################
##############################################
#ezafe kardan string ha b hm
a = "Hello"
b = "World"
c = a + b
print(c)

##############################################
##############################################
#method format
kilo = 3
mqdar_darkhast = 567
kolesh = kilo*mqdar_darkhast
myorder = "man goje {} kiloee mikham b meqdare {} kilo k kolesh mishe {} ."
print(myorder.format(kilo, mqdar_darkhast, kolesh))


##############################################
##############################################
#DARBARE ESCAPE VA BBAGHI METHOD HA SEARCH BFARMAEEN
