# 3. Student I.D. checker
import re

VALID-ID = r'^\d{2}-\d{5}$'
ID = input("Enter your ID: ")

if re.match(VALIDID, ID):
    print(f"Valid ID")
else:
    print(f"Invalid ID")
