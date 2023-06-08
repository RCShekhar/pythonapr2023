class Computer:
    cpu = "Intel i7"
    storage = '512GB'
    memory = "16GB"

    def switch_on(self):
        print(f"{self.make} computer Switched ON")

    def switch_off(self):
        print(f"{self.make} computer Switched OFF")

class HPComputer(Computer):
    HPUtilty = "HP Utility"
    make ="HP"


class DellComputer(Computer):
    DellUtilty = "Dell Utility"
    make = "DELL"



hp = HPComputer()
# print(dir(hp))
hp.switch_on()
hp.switch_off()

dell = DellComputer()
# print(dir(dell))
dell.switch_on()
dell.switch_off()



print(isinstance(hp, HPComputer))
print(isinstance(hp, DellComputer))
print(isinstance(hp, Computer))
print(isinstance(dell, Computer))