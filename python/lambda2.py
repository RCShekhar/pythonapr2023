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


# print(operation(10,20, operator='*'))

addition = lambda n1,n2: operation(n1,n2,operator="+")
multiplication = lambda n1,n2:operation(n1,n2,operator="*")

print(addition(5,6))
print(addition(9,10))

print(multiplication(10, 5))
print(multiplication(16, 5))


evens = lambda *args : [e for e in args if e%2!=0 ]
print(evens(1,2,3,4,5,6,7,8,9,10,11,12,13,2,6,4,8,9,5,))

"hello"