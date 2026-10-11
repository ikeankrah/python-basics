# Factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

for n in [0, 1, 5, 10]:
    print(f"{n}! = {factorial(n)}")
