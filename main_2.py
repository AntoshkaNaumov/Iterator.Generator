def flatten(data):

    nested = True
    while nested:
        new = []
        nested = False
        for i in data:
            if isinstance(i, list):
                new.extend(i)
                nested = True
            else:
                new.append(i)
        data = new
    return data

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None], ]
    numbers_iterator = iter(nested_list)
    print(next(numbers_iterator))
    print(next(numbers_iterator))
    print(next(numbers_iterator))

    for item in flatten(nested_list):
        print(item)