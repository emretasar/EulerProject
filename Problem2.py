# Emre Tasar -> 23.01.2022
# Even Fibonacci numbers

fibonacci = [1, 1]
sum = 0
while(True):
    if(fibonacci[-1] + fibonacci[-2] > 4000000):
        break
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if(fibonacci[-1] % 2 == 0):
        sum += fibonacci[-1]

print(sum)