# Emre Tasar -> 23.01.2022
# Largest prime factor

from math import sqrt

def isprime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

prime_factors = []
interest = 600851475143 
for i in range(2, int(sqrt(interest))):
    if(interest % i == 0) and isprime(i):
        prime_factors.append(i)

print(max(prime_factors))
print(prime_factors)
