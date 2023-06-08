disc_data = [
    "10|89.6",
    "11|99.5",
    "12|98.2"
]

def read_disc_gen():
    for element in disc_data:
        e = element.split('|')
        d = {
            'id':e[0],
            'score':e[1]
        }
        yield d

# def read_disc_fun():
#     l = []
#     for element in disc_data:
#         e = element.split('|')
#         d = {
#             'id':e[0],
#             'score':e[1]
#         }
#         l.append(d)

#     return l


i=13
result = read_disc_gen()
students = []
for student in result:
    students.append(student)
    print(student)  

    if i<=17:
        disc_data.append(f"{i}|{i+80.0}")
        i+=1


print(students)