def binary_exponentiation(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result

a = 3
b = 10

result = binary_exponentiation(a, b)
print(result)