# print()
# print('Hello', 'world','my number', 10)
# print('hello world')


# def add(number1, number2):
#     return number1 + number2


def add(*numbers):
    result = 0
    for number in numbers:
        result += number

    return result


print(add())
print(add(1))
print(add(1,2,3,4,5))
print('*'*100)

# Another way to suppy actual arguements
mynumber = [6,8,3,5,9,0]

sum = add(*mynumber)
print(sum)

print(add(6,8,3,5,9,0))

print('*'*100)

def concat(*strings):
    result = ''
    for string in strings:
        result += string

    return result

print(concat('hello', 'world', '!!'))



