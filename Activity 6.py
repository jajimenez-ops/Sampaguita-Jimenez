# 1. Payment Method Checker

valid_method = ("gcash","cash","card")

method = input("How would you like to pay? ")
if method in valid_method:
    print(f"Valid Method")
else:
    print(f"Invalid Method")


