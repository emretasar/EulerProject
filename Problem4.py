
def isPalindrome(number):
    
    number_str = str(number)
    number_length = len(number_str)
    if number_length % 2 == 0:
        largest_index = int(number_length / 2) - 1
    else:
        largest_index = int(number_length / 2)
    
    for i in range(largest_index + 1):
        if number_str[i] != number_str[-i-1]:
            return False 

    return True


l = []
for i in range(900, 1000):
    for j in range(900, 1000):
        if isPalindrome(i * j):
            l.append(i*j)

print(max(l))
