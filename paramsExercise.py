params = ('the addition', 'of given values', 10,20, 30, 'second set', 'results is', 20,40.2,50)
# # step1 prepare like this 
segments = (['the addition', 'of given values'], [10,20,30], ['second set', 'results is'], [20,40.2,50])
# # for segment in segments:
# #     if segment type is string:
# #         concat(*segment)
# #     if segment type is numeric:
# #         add(*segment)
# #step 2
# segments = ('the addition of given values', 60, 'second set result is', 110.2)
# concat(*segments)
# # step 3
# result = 'the addition of given values 60 second set result is 110.2'



def concat(*strings):
    result = ''
    for string in strings:
        result += string
        result += ' '

    return result.strip()

def add(*numeric):
    result = 0
    for x in numeric:
        if isinstance(x, int) or isinstance(x,float):
            result += x

    return result


string_types = [str]
numeric_types = [int, float]
def concat_and_add(*args):
    segments = []
    current_type = [None]
    current_segment =[]

    for arg in args: # arg = 20
        if type(arg) not in current_type: # int not in [int, float]
            current_type = string_types if type(arg) in string_types else numeric_types # current_type = numeric_type
            if current_segment: 
                segments.append(current_segment) 
            current_segment=[] # []

        current_segment.append(arg) #[20, 40.2, 50]
    else:
        if current_segment:
            segments.append(current_segment)

    result = []
    for segment in segments:
        if type(segment[0]) in string_types:
            result.append(concat(*segment))
        else:
            result.append(add(*segment))

    #final_result = ' '.join([str(i) for i in result])
    template = "{} " * len(result)
    final_result = template.format(*result)
    print(final_result)

    



result = concat_and_add(*params)
