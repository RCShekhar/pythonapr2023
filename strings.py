s = "hello"
ovels = ''
consonents = ''

# for c in s:
#     if c in 'aeiou':
#         ovels += c
#     else:
#         consonents += c

ovels = ''.join([c for c in s if c in 'aeiou'])
consonents = ''.join([c for c in s if c not in 'aeiou'])

print(ovels)
print(consonents)
