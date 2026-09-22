try:
    valid_age = range(12,18)
    age = int(input("Enter your age: "))
    if age in valid_age:
        print(f"Valid Age")
    else:
        print(f"Invalid Age. Age must be between 12 and 18")
except ValueError:
    print(f"Invalid Age. Please enter a whole number")