class Computer:
    cpu = "Intel i7"
    memory = "16GB"
    storage_type = "SSD"
    storage_capacity = "1TB"
    serialno = '12345'
    model = "macbook air 2020"

    def switch_on(self):
        print('*'*50)
        print("Computer turned on")
        print("The configuration of your computer is:")
        print("CPU", self.cpu)
        print("Memory", self.memory)
        print("storage", self.storage_capacity)

    def switch_off(self):
        print("Computer is shutting down")

    def update_config(self, cpu, memory, storage):
        self.cpu = cpu
        self.memory = memory
        self.storage_capacity = storage


shekhar_computer = Computer()
ravi_computer = Computer()

ravi_computer.update_config('Apple M1', '8GB', '512GB')
# #shekhar_computer.switch_on()
# Computer.switch_on(shekhar_computer)
shekhar_computer.switch_on()
ravi_computer.switch_on()

shekhar_computer.switch_off()
ravi_computer.switch_off()
# Computer.switch_on() takes 0 positional arguments but 1 was given