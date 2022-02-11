from math import sqrt

def isprime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

number = 2
summation = 0
while(number < 2000000):
    if(isprime(number)):
        summation += number
    number += 1

print(summation)