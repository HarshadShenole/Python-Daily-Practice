import re
text = " I am learning Python"
result = re.search("Python",text)
print(result.group())