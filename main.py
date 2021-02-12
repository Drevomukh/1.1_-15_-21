import math

x = 33
y = -25

a = (x ** 5 - 68 * y ** 7 + 46)
b = (x ** 2 - ( x ** 5 ) / 13)
c = y - y ** 3

result = math.sqrt(a) - b - c

print(f"{result:.2e}")
