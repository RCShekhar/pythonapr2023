# number = int(input("Enter a number:"))

# f = 2
# factors = []

# while f < number:
#     if f >= number//2:
#         break
#     if number%f == 0:
#         factors.append(f)    
#     f += 1

# if len(factors) == 0:
#     print("The number", number, "is a prime number")
# else:
#     print("The number", number, "is not a prime number")

for number in range(2, 101):
    # number = int(input("Enter a number:"))
    f = 2
    while f <= number//2:
        # print("Checking", f)
        if number%f == 0:
            print("The number", number, "is not a prime number")
            break
        f += 1
    else:
        print("The number", number, "is a prime number")

print("End of the program")


