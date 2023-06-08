# 'the addition', 'of given values', 10,20, 30
# "the addition of given values 60"

def add(*numbers):
    result = 0
    for number in numbers:
        result += number

    return result

def concat(*strings):
    result = ''
    for string in strings:
        result += string

    return result

def addition(*params):
    result = ''
    
    
    return result

print(addition('the addition ', 'of given values is ', 10, 20, 30))


params = ('the addition', 'of given values', 10,20, 30, 'second set', 'results is', 20,40.2,50)
# step1 prepare like this 
segments = (['the addition', 'of given values'], [10,20,30], ['second set', 'results is'], [20,40.2,50])
# for segment in segments:
#     if segment type is string:
#         concat(*segment)
#     if segment type is numeric:
#         add(*segment)
#step 2
segments = ('the addition of given values', 60, 'second set result is', 110.2)
concat(*segments)
# step 3
result = 'the addition of given values 60 second set result is 110.2'