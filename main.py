# 1. Написать итератор, который принимает список списков,
# и возвращает их плоское представление, т.е последовательность
# состоящую из вложенных элементов.
# 2. Написать генератор, который принимает список списков,
# и возвращает их плоское представление

def recursive_flatten(arr):

    for i in arr:
        if isinstance(i, list):
            yield from recursive_flatten(i)
        else:
            yield i

class FlatIterator():

    def __init__(self, list):
        self.stop = False
        self.list = list
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stop:
            while self.i < len(self.list):
                if self.j < len(self.list[self.i]):
                    result = self.list[self.i][self.j]
                    self.j += 1
                    return result

                self.i += 1
                self.j = 0
            self.stop = True
        raise StopIteration


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None], ]
    for item in FlatIterator(nested_list):
        print(item)
    print('_______________________________________')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('_______________________________________')
    for item in recursive_flatten(nested_list):
        print(item)
    print('_______________________________________')
    flat_list = [item for item in recursive_flatten(nested_list)]
    print(flat_list)
