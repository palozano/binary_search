import random

from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # Taken from itertools recipes:
    # https://docs.python.org/3/library/itertools.html#itertools-recipes
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def main():
    students = [x for x in range(1, 9)]

    random.shuffle(students)

    pairs = list()

    for first_student, second_student in grouper(students, 2):
            pairs.append((first_student, second_student))

    print(pairs)


if __name__ == '__main__':
    main()
