# *
# **
# ***
# ****
# *****

# 1. Pattern has 5 lines, and last line has 5 stars (n lines -> n stars)
# 2. nuber of stars for each line is depends on line number
# 3. its look like a two dimentional shape


lines = int(input("Enter number of line you want to print:"))

for line in range(1,lines+1):
    print('*' * (line))
    # for colum in range(line+1):
    #     print("*", end='')
    # print('', end='\n')