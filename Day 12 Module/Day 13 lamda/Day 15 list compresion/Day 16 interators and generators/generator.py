def number():
    yield 20
    yield 30
    yield 40

gen = number()

print(next(gen))
print(next(gen))
print(next(gen))
    