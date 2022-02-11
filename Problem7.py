from math import sqrt

def isprime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

interested_prime = 10001

prime_counter = 0
number = 2
while(prime_counter < interested_prime):
    if isprime(number):
        prime_counter+=1
        number+=1
    
    else:
        number+=1

print(number-1)