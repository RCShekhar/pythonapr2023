# n! = n*(n-1)*(n-2)....  = n*(n-1)!
# 5! = 5*4*3*2*1 = 5*4!
# 4! = 4*3*2*1 = 4*3!
# 3! = 3*2*1 = 3*2!
# 2! = 2*1
# 1! = 1
# 0! = 1


import time

def timeit(func):
    def inner(*params, **kwargs):
        stime = time.time()
        r = func(*params, **kwargs)
        etime = time.time()
        print(f"output for {params} taken {etime-stime} secs")
        return r
    inner._copy = func
    return inner


@timeit
def factorial(n): # factorial = timeit(factorial)
    if n<=1:
        return 1
    original_fact = factorial._copy
    result = n*original_fact(n-1)
    return result

print(factorial(10))



