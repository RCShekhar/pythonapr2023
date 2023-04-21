# l = [1,2,3,4,5]

# ls = [each_number**2 for each_number in l]
# print(ls)


l2 = list(range(1,21))
print(l2)

even_numbers = tuple(number for number in l2 if not number%2)
print("even number lis is:",even_numbers)
odd_numbers = tuple(number for number in l2 if number%2)
print("odd number lis is:",odd_numbers)

