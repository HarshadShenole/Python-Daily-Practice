import re
number = "9876543210"
if re.fullmatch(r"\d{5}",number):
    print("valid Number")
else:
    print("Invalid")