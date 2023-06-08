
# def decorator(whatever_the_func):
#     def inner():
#         print('*' * 100)
#         whatever_the_func()
#         print('*' * 100)

#     return inner


# @decorator
# def printname():
#     print("Hello World")


# @decorator
# def greet():
#     print("Hello")


# printname()
# greet()

import time

def timeit(func):
    def inner(*params, **kwargs):
        stime = time.time()
        r = func(*params, **kwargs)
        etime = time.time()
        print(f"the process is completed in {etime-stime} secs")
        return r

    return inner


@timeit
def process_Data():
    huge_data=[1,2,3,4,5]
    for each_element in huge_data:
        print(each_element)

process_Data()


@timeit
def add(a, b): # add=timeit(add)
    print(a+b)

add(1,3) 
add(5,8)


@timeit
def subtract(first=10, second=5):
    print(first-second)

subtract(second=20, first=50)

@timeit
def div(n1, n2):
    return n1/n2

print(div(10,20))