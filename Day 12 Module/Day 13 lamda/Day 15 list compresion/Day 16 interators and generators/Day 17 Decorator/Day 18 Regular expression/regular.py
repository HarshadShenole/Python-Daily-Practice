import re
text = "My phone number is 987665767"
result = re.search(r"\d+", text)
print(result.group())