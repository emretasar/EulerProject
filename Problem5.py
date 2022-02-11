# Emre Tasar -> 23.01.2022
# Smallest multiple

from math import gcd

def gre_com_div(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


product = 1
for i in range(2, 20):
    if(product % i == 0):
        continue
    elif(product % i != 0):
        greatest_common_div = gre_com_div(i, product)
        if(greatest_common_div == 1):
            product *= i
        elif(greatest_common_div != 1):
            product *= greatest_common_div 

print(product)