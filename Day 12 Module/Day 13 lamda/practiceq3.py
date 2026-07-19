from functools import reduce
marks = [35,42,55,80,25]
result = reduce(lambda x ,y : x+y,marks)
print(result)

