#Step 1: Import Math Library
import math
#Step 2: Get the required values
print("Input your x1")
x1 = float(input())
print("Input your x2")
x2 = float(input())
print("Input your y1")
y1 = float(input())
print("Input your y2")
y2 = float(input())
#Step 3: Calculate the distance with the formula
x3 = x2 - x1
y3 = y2 - y1
total = pow(x3,2) + pow(y3,2)
final = math.sqrt(total)
#Step 4: Print the output
print(f"The distance between the coordinates is {final:.2f}")

# Refelction: We have to add comments so that they understand the work and what is happening more clearly.
