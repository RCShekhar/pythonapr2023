
# Haoop
def map(f, input):
    return [f(e) for e in input]


# find squares of all the given numbers

ip = [4,5,6,7,8]

# def sq(e):
#     return e**2

# sq = lambda e: e**2

# print(lambda e: e**2)

iseven = lambda e: True if e%2==0 else False

print(iseven(10))
print(iseven(11))

print(map(lambda e: e**2, ip))