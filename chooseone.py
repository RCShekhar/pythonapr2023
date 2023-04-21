
name = input("Enter a name to react:")

print("\nChoose from below menu")
print("1. Greet")
print("2. Shout")
print("3. Stay calm")

print("\n")
menu = input("Enter your option from above menu:")

if menu == '1':
    msg = "Hello " + name + "!!"
    print(msg)
elif menu == '2':
    msg = name.upper() + "..!!!"
    print(msg)
elif menu == '3':
    msg = 'SHHH.....'
    print(msg)
else:
    msg = "Wrong option choosen"
    print(msg)
