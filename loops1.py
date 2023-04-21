
# add 1 to 10 numbers

# iterations = 150
# n = 1
# result = 0

# while n<=iterations:
#     result += n # result = result + n
#     print("Added", n)
#     n += 1 # n = n + 1

# print("Result is", result)

usb_device_available = False
usb_connected = False
while not usb_connected:
    print("Checking for usb device")
    if usb_device_available:
        usb_connected = True


data = get(data)
while is_data_available:
    display(data)
    data = get(data)
    if data is None:
        is_data_available = False

for data in get():
    display(data)


# lines = 5
# no of stars in a line depends on the line number

*
**
***
****
*****