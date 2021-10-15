"""
project euler
second
majmo fibonachi haye zire 4 milion
amma hatma bayad mazrabi az 2 bashan
"""
n1 = 1
n2 = 2
count = 0 #count shomarandast
total = 0
while count < n1 < 4000000:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1
    #shomaresh count baes mishe if ham jelo bere
    #ham shart baqarar bashe
    if n1%2 == 0 and count < n1 < 4000000:
        total += n1
    elif n2 == 2:
        total += 2
    else:
        total += 0
print("jame morede nazar =",total)