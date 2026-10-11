# Check whether numbers are even or odd
def even_or_odd(n):
    return "even" if n % 2 == 0 else "odd"

for n in [1, 2, 7, 10, 33]:
    print(n, "is", even_or_odd(n))
