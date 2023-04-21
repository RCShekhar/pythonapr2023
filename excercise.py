# 2.write a program to check if last digit of given number is 3 or not

# a = 12300

# if a%100 == 0:
#     print("the number can be divided by 100")
# else:
#     print("the number cannt be divided by 100")



# 3. Write a program to calculate tax based on tax rates given below.
# > 100000 - 15% 
# 50000 to 100000 - 10%
# <= 50000 - 5%


transaction_amount = float(input("Enter Tranasaction value:"))
# 200000
ta = transaction_amount # ta = 200000
tax_amount = 0

if transaction_amount < 0: # False
    print("Invalid Transaction amount")
    exit()

if transaction_amount > 100000: #200000
    taxable_amount = transaction_amount - 100000 # taxable amount = 100000
    tax_amount = tax_amount + taxable_amount * 0.15 # tax amount = 15000
    transaction_amount = transaction_amount - taxable_amount # transaction amount = 100000

if transaction_amount > 50000: #100000 > 50000 which is True
    taxable_amount = transaction_amount - 50000  #taxable amount = 50000
    tax_amount = tax_amount + taxable_amount * 0.1 # tax will be 15000 + 5000 = 20000
    transaction_amount = transaction_amount - taxable_amount # new transaction amount 50000

if transaction_amount > 0: # 50000 
    tax_amount = tax_amount + transaction_amount * 0.05 # 20000 + 2500 = 22500
  


print("Tax on", ta, "is", tax_amount)