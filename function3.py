

def read_dict(key, default="Nothing Found"):
    d = {'one':1, 'two':2}
    result = d.get(key)
    if result is None:
        result = default
    print(f"The value for given key:{key} is {result}")




