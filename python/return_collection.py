def getlist(start, end):
    l = []
    i=start
    while i<= end:
        l.append(i)
        i+=1
    
    return l

lst = getlist(1,10)
print(type(lst), lst)