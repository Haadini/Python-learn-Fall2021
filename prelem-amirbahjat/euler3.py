"""
project euler
third
bozorgtarin amele aval adad 600851475143 beyabid
"""
x = 600851475143
y = 2
while y * y < x:
    while x % y == 0:
        x = x / y
    y = y + 1
print (int(x))
#niaz b fekr dare =)