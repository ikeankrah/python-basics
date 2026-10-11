# Find the largest number in a list
numbers = [12, 45, 7, 89, 23, 54]

largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n

print("Largest (loop):", largest)
print("Largest (max):", max(numbers))
