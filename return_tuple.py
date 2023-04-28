#Bhavani

print("Bhavani".center(100,'*'))
def tuple_values(start, end):
    t_result = ()
    while start !=end:
        t_result += start,
        start+=1
    return t_result

print(tuple_values(1, 11))



print("Rimjhim".center(100,'*'))
#Rimjhim
def getlist(start,end):
    t = ()
    i=start
    while i<= end:
       t = t + (i,)
       i += 1
    print(t)
    return t
    

print(getlist(1,10))


print("Ismail".center(100,'*'))
def tuple_values(start, end):
    return tuple(range(start,end))

print(tuple_values(1,20))