l2 = list(range(1,21))
print(l2)

# indexes starts with 0 and ends with n-1 where n is the number of elements in a collection

even_numbers = []
odd_numbers = []
i = 0
while i < len(l2):
    if l2[i]%2:
        odd_numbers.append(l2[i])
    else:
        even_numbers.append(l2[i])
    i += 1

print("Even numbers", even_numbers)
print("Odd numbers", odd_numbers)
