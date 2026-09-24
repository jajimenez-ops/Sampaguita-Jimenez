import math

print("Input your x1")
x1 = float(input())
print("Input your x2")
x2 = float(input())
print("Input your y1")
y1 = float(input())
print("Input your y2")
y2 = float(input())

x3 = x2 - x1
y3 = y2 - y1
total = pow(x3,2) + pow(y3,2)
final = math.sqrt(total)
print("The distance between the coordinates is {final:.2f}")
