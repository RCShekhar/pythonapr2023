class Computer:
    cpu = "Intel i7"
    memory = "16GB"
    storage_type = "SSD"
    storage_capacity = "1TB"
    serialno = '12345'
    model = "macbook air 2020"

    def switch_on():
        print("Computer turned on")
        print("The configuration of your computer is:")
        print("CPU", cpu)
        print("Memory", memory)
        print("storage", storage_capacity)

    def switch_off():
        print("Computer is shutting down")


shekhar_computer = Computer()
ravi_computer = Computer()

# print(type(shekhar_computer))
# print(type(10))

ravi_computer.cpu = 'Apple M1'
ravi_computer.memory = '8GB'
print("Ravi's computer")
print(ravi_computer.cpu)
print(ravi_computer.memory)
print(ravi_computer.model)

print("Shekhar's computer")
print(shekhar_computer.cpu)
print(shekhar_computer.memory)
print(shekhar_computer.model)