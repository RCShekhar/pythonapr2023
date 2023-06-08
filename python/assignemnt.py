#Question: ('the numeric addition', 'of given values', 10,20, 30)
('addition of first seto f numbers', 10, 20, 30,'second set of numbers', 40,50,60)
"addition of first seto f numbers 60 second set of numbers 150"

# Ismail
def addition(*params):
    sum = 0
    for x in params:
        if type(x) == int or type(x) == float:
           sum+=x
        else:
            print(x,end='')
    return sum

print(addition('the addition ', 'of given numbers are', 10,20,20,30))

# Amala
def addition(*params):
    for value in params:
        if type(value) == str:
            result1 += value
        if type(value) == int:
            result2 += value
    return result1 + str(result2)

# Jyothsna
def addition(*params):
    result = sum(params)
    return f"the addition of given values is {result}"

print(addition(10,20,30))

# Pavithra
def addition(*params):
    result = ''
    sum_val = 0
    for i in params:
        if type(i) == str:
            result+=i + ' '
        if type(i) == int:
            sum_val+= i
    result = result + str(sum_val)

    return result

print(addition("the addition", "of given value is ", 10,20,30))