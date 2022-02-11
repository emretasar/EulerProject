# Emre Tasar -> 23.01.2022
# Special Pythagorean Triplet

for a in range(1, 1000):
    for b in range (a + 1, 999):
        c_squared = a**2 + b**2
        c = c_squared ** 0.5

        if a + b + c == 1000:
            product = a * b * c
            print(product)
            break