import re
email = "abc@gmail.com"
pattern = r"\w+@\w+"
if re.fullmatch(pattern,email):
    print("valid")
else:
    print("Invalid")