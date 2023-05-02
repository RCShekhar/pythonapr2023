# def n_numbers(limit):
#     l = []
#     start = 1
#     while start <= limit:
#         l.append(start)
#         start += 1

#     return l


def n_numbers(limit):
    next_number = 1
    while next_number <= limit:
        yield next_number
        next_number += 1

gen_obj = n_numbers(100)

for number in gen_obj:
    print(number)