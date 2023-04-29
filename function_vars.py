def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def rem(a,b):
    return a%b

def doit(ip1, ip2, action):
    return action(ip1, ip2)

r = doit(10,20, rem)
print(r)