# Sum of a list, with and without sum()
numbers = [4, 8, 15, 16, 23, 42]

total = 0
for n in numbers:
    total += n

print("Loop total:", total)
print("sum() total:", sum(numbers))
