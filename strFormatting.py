# a = 10
# b=20

# c = a+b

# message = "The result is " + str(c)
# print(message)

#format method

name = "John"
id = 10
score = 98.5

msg_template = "the sudent {} with id {} scored {}"
message = msg_template.format(name,id,score)
print(message)

name = "Ravi"
id = 11
score = 97.5

message = msg_template.format(name, id, score)
print(message)


print("*"*80)


msg_template = "Hello {}, your details are as below\nName: {} \n Id: {} \nScore: {}"
msg = msg_template.format(name,name,id,score)
print(msg)

print('-'*80)

msg_template = "Hello {0}, your details are as below\nName: {0} \n Id: {1} \nScore: {2}"
msg = msg_template.format(name,id,score)
print(msg)

print('-'*100)

msg_template = "Hello {n}, your details are as below\nName: {n} \n Id: {i} \nScore: {s}"
msg = msg_template.format(n=name, i=id, s=score)
print(msg)

print('='*100)

msg = f"Hello {name}, your details are as below\nName: {name} \n Id: {id} \nScore: {score}"
print(msg)

