class Father:
    father_name = "Ravi"
    salary = 10000


class Mother:
    mother_name = "Swathi"


class Child(Mother, Father):
    child_name = "Rajesh"


c = Child()

print(c.child_name, c.salary)
