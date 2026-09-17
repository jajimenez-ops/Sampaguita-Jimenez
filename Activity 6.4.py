# 4. PIN Validator

PIN = int(input("Create a PIN that is 6 - digits long: "))

if len(PIN) == 6:
    print(f"Valid PIN: {PIN}")
else:
    print(f"Invalid PIN: {PIN}")
