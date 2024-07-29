def mygenerators():
    for i in range(100):
        yield i
gen=mygenerators()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))