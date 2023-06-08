def operation(number1, number2, operator='+'):
    if operator == '+':
        operation_performed = "Addition"
        result = number1+number2
    elif operator == '-':
        operation_performed = "Subtraction"
        result = number1 - number2
    elif operator == '*':
        operation_performed = "Multiplication"
        result = number1 * number2
    elif operator == '/':
        operation_performed = "Division"
        result = number1/ number2
    else:
        operation_performed = "Invalid Operation"
        result = None
    print("Operation performed is", operation_performed, end=' ')
    return result

print(operation(10,20))
print(operation(10,20, '*'))
print(operation(10,20, operator='+'))
# operation(20, operator='-', number1=10)
print(operation(10, operator='/', number2=20))
print(operation(operator='/', number2=30, number1=60))
print(operation(10,20, 'Hello'))
