# factorial of a given number

def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact *= i

    print("Factorial of",number,"is",fact)


print("Start")
factorial(7)
factorial(8)
factorial(9)
print("End")
