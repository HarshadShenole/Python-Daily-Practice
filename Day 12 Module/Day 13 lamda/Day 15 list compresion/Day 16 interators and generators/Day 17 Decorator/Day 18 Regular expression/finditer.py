import re
text = "cat dog cat"
for i in re.finditer("cat ", text):
    print(i.start(),i.group())