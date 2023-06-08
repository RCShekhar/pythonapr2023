# def func(person1, person2, person3):
#     print(person1, person2, person3)

# def func2(*perosn):
#     print(perosn)

# work1 = 1
# work2 = 2.3
# work3 = "hello"

# # func(work1, work2, work3)
# # func(work3, work1, work2)
# # func2(work1, work2, work3)

# func(person3=work1, person2=work3, person1=work2)

# def func3(**person):
#     print(person)

# func3(second=work1, fist=work3, third=work2)


def myfunc(*args, **kwars):
    result = ''
    for key in kwars:
        result += kwars[key]

    print(args)

    print(result)

# myfunc(1,2.5,'hi')
# myfunc(1,2, x='hello', y='hi')
# myfunc(a=1, b=2.3, c='hi')
# myfunc()

myfunc(
    {'a':10,'b':20}, 
    {'x':103, 'y':11.4}, 
    str1='Hello', 
    str2='world'
)









