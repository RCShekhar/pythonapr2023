a = int(
    input("Enter first number:")
)

b = int(
    input("Enter second number:")
)

c = int(
    input("Enter third number:")
)


# if a > b:
#     if a > c:
#         print("a",a,"is the largest of three")
#     if c > a:
#         print("c",c,"is the largest of three")

# if b > a:
#     if b > c:
#         print("b",b,"is the largest of three")
#     if c > b:
#         print("c",c,"is the largest of three")

# if a>b:
#     if a>c:
#         print("a",a,"is the largest of three")
#     else:
#         print("c",c,"is the largest of three")
# else:
#     if b>c:
#         print("b",b,"is the largest of three")
#     else:
#         print("c",c,"is the largest of three")

if a>b:
    if a>c:
        print("a",a,"is the largest of three")
    elif a<c:
        print("c",c,"is the largest of three")
    else:
        print("both a and c are same", a)
else: # a<b or a == b
    if b>c:
        if b==a:
            print("both a and b are same", a)
        else:
            print("b",b,"is the largest of three")
    elif b<c:
        print("c",c,"is the largest of three")
    else: #b==c (b==a, b>a)
        if b==a:
            print("all the three numbers are same", a)
        else:
            print("both b and c are same", b)


