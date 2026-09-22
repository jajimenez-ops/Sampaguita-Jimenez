try:
    valid_grade = range(7,12)
    age = int(input("Enter your age: "))
    if age in valid_grade:
        print(f"Valid Grade.")
    else:
        print(f"Invalid Grade. Must be between 7 and 12.")
except ValueError:
    print(f"Invalid Grade. Please enter a whole number.")