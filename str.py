input_string = input("Enter your string:")

p = "!@./'\""

output =''
for each_char in input_string:
    if each_char not in p:
        output += each_char

print(output)
