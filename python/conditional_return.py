def is_prime(number):
    for f in range(2, number//2+1):
        if number%f == 0:
            return False      
    return True

# def is_prime(number):
#     result = True
#     for f in range(2, number//2+1):
#         if number%f == 0:
#             result = False
#             break
             
#     return result


n=6
if is_prime(n):
    print(f"the number {n} is a prime")
else:
    print(f"the number {n} is not a prime")