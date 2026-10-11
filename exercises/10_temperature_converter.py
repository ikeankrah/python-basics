# Celsius <-> Fahrenheit converter
def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

for c in [0, 25, 37, 100]:
    print(f"{c}°C = {c_to_f(c):.1f}°F")

print(f"98.6°F = {f_to_c(98.6):.1f}°C")
