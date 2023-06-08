# def f(a,b,c,x=1,y=2,z=3):
#     print("the given values are", a,b,c,x,y,z)


# f(c=9,a=8,b=7)
# f(0,1,5, 4,7,5)


# 4) Write a function that takes in a dictionary as a keyword  argument and returns the value of the key "name".


def find_value(key, d={}):
    return d.get(key)

r = find_value('name')
print(r)

d = {'name':'Rakesh', 'id':10, 'score':98.3}
r = find_value('name', d)
print(r)