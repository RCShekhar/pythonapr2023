
class Computer:
    message = "Hello World"
    def __init__(self, cpu, memory, storage, model, serial, make):
        self.make = make
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.model = model
        self.serial = serial



class Dell(Computer):
    def __init__(self, cpu, memory, storage, model, serial, make):
        super().__init__(cpu, memory, storage, model, serial, make)
    


computer1 = Computer('Intel Xenon', "32GB", "1TB - SSD", "Inspiron X series", "5X67GT344", "DELL")
computer2 = Computer('Intel core i9', "16GB", "12B - SSD", "Inspiron 5000 series", "5X67GT354", "DELL")

dell_computer = Dell('Intel core i9', "16GB", "12B - SSD", "Inspiron 5000 series", "5X67GT354", "DELL")

print(dell_computer.message)
print(dell_computer.cpu)
dell_computer.private_message = " Priveate message"

print(dell_computer.private_message)



print(computer1.make,
      computer1.cpu, 
      computer1.memory,
      computer1.storage
      )

print(computer2.make,
      computer2.cpu, 
      computer2.memory,
      computer2.storage
      )
