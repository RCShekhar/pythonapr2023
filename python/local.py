gv = 20


def func(n):
    gv = n
    print("inside function local",gv)
    print("insiede function gv", gv)

func(10)

print("outsice function gv", gv)
# print("outside function local", var)