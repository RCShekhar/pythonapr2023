# Haoop
def map(f, input):
    return [f(e) for e in input]

def reduce(f, input):
    result = None
    for e in input:
        result = f(result, e)

    return result


# sum of squares of a list of number

l = [4,3,6,4]

def squre(num):
    return num**2

def qube(nuber):
    return nuber ** 3

def half(number):
    return number/2

def sum(a, b):
    if a is None:
        a = 0
    if b is None:
        b = 0
    return a + b

def multi(a, b):
    if a is None:
        a = 1
    if b is None:
        b = 1
    return a*b


mapout = map(half, l)
print(mapout)
final_result = reduce(multi, mapout)
print(final_result)


string = "hello"
def upper(c):
    return c.upper()

def build_string(a, b):
    if a is None:
        a = ''
    if b is None:
        b = ''

    return a+b

output = map(upper, string)
r = reduce(build_string, output)
print(r)

