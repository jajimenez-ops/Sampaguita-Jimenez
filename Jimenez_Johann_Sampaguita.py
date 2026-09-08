# The code starts by saking for side A and B
import math
a = input("Enter side A: ")
b = input("Enter side B: ")

# Now it calculates the hypotenuse

c2 = pow(a,2) + pow(b,2)
c = math.sqrt(c2)
# Then its outputs the answer
print(f"The hypotenuse is {c:.2f}")
