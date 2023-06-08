def outer():
    outer_var = 10

    def inner():
        nonlocal outer_var
        inner_var = 15
        outer_var = 20
        print("outer var", outer_var)
        print("inner var", inner_var)

    inner()

    print("outer",outer_var)
    #print("inner", inner_var)

outer()

