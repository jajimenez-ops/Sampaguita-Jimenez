
#The Try is to just detect Value errors
try:
    #Greets the user
    print(f"Hello user.")
    #Asks and defines the variable
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    c = 0
    d = 0

    #First Function - Finds the sum
    def sum():
        global c
        c = a + b
        print(f"The sum of {a} and {b} is {c}")
    #Second Function - Finds the difference
    def difference():
        global d
        d = a - b
        print(f"The difference of {a} and {b} is {d}")
    sum()
    difference()
except ValueError:
    print("Please enter a real number")
