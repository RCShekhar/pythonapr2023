students = [
    {
    'name':'Rakesh',
    'id':10,
    'score':93.4
    },
    {
    'name':'John',
    'id':11,
    'score':98.2
    },
    {
    'name':'Philip',
    'id':12,
    'score':96.8
    }
]

template = "Hello {n}, your details are as below\nName: {n} \n Id: {i} \nScore: {s}"

for student in students:
    msg = template.format(
        n=student.get('name'),
        i=student.get('id'),
        s=student.get('score')
    )
    print(msg)


