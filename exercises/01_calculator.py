# Simple calculator
def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return "Cannot divide by zero" if b == 0 else a / b
    return "Unknown operator"

print(calculate(10, 5, "+"))
print(calculate(10, 5, "-"))
print(calculate(10, 5, "*"))
print(calculate(10, 0, "/"))
