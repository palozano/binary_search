# Random Search
#
# def find(elements, value):
#     while True:
#         random_element = random.choice(elements)
#         if random_element == value:
#             return random_element
#
#
# Linear Search
#
# def find_index(elements, value):
#     for index, element in enumerate(elements):
#         if element == value:
#             return index
#
# Python already has linear search: list_name.index(item_to_look_up)
# or in a more pythonic way: 'item_to_look up' in list_name --> True/False
# (Note: th operator 'in' with sets does a hash-based search, and it can
# work with any iterable.)
#
#
# Binary Search
#
# You can use the bisect module from Python, based on the bisection
# method for finding roots of functions, to perform binary search.
# (Note: you must sort the list first.)
#
# As a function:
#
# def find_index(elements, value):
#     index = bisect.bisect_left(elements, value)
#     if index < len(elements) and elements[index] == value:
#         return index
#
# Or just using:
#
# sorted_list = [1, 2, 3]
# index_of_item = bisect.bisect_left(sorted_list, 'item_to_look_for')
#
# To search by key, you need a separate list of keys. It'd be good to use
# # a helper class to help you not having code duplication:
#
# class SearchBy:
#     def __init__(self, key, elements):
#         self.elements_by_key = sorted([(key(x), x) for x in elements])
#         self.keys = [x[0] for x in self.elements_by_key]
#
#     def find(self, value):
#         index = bisect.bisect_left(self.keys, value)
#         if index < len(self.keys) and self.keys[index] == value:
#             return self.elements_by_key[index][1]
#
# where key is a function pased to the __init__() function


# import random
# import math
# import importing


def load_names(path):
    with open(path) as text_file:
        return text_file.read().splitlines()


names = load_names('names.txt')
sorted_names = load_names('sorted_names.txt')


# We could construct some functions to get a similar behavior
# of the bisect module.

# To find an index, we'd do:
# (Note: we can search by a key, if we previously sort by it.)

def identity(element):
    # This can be a lambda function --> lambda x: x
    return element


def find_index(elements, value, key=identity):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = key(elements[middle])

        # if math.isclose(elements[middle], value):
        if middle_element == value:
            return middle

        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1


# But we need two functions more,
# one to see if an element is contined in a set
def contains(elements, value, key=identity):
    return find_index(elements, value, key) is not None


# and another to find the element
def find(elements, value, key=identity):
    index = find_index(elements, value, key)
    return None if index is None else elements[index]


# We might want to mimic bisect_right() and bisect_left() too:
def find_leftmost_index(elements, value, key=identity):
    index = find_index(elements, value, key)
    if index is not None:
        while index >= 0 and key(elements[index]) == value:
            index -= 1
        index += 1
    return index


def find_rightmost_index(elements, value, key=identity):
    index = find_index(elements, value, key)
    if index is not None:
        while index < len(elements) and key(elements[index]) == value:
            index += 1
        index -= 1
    return index


def find_all_indices(elements, value, key=identity):
    left = find_leftmost_index(elements, value, key)
    right = find_rightmost_index(elements, value, key)
    if left and right:
        return set(range(left, right + 1))
    return set()


def find_leftmost(elements, value, key=identity):
    index = find_leftmost_index(elements, value, key)
    return None if index is None else elements[index]


def find_rightmost(elements, value, key=identity):
    index = find_rightmost_index(elements, value, key)
    return None if index is None else elements[index]


def find_all(elements, value, key=identity):
    return {elements[i] for i in find_all_indices(elements, value, key)}

# This allow you to locate elements on the list, and also
# to retrieve those elements.


# You can implement a recursive function for finding if an element is
# contained in a set:
def contains_rec(elements, value, left, right):
    if left <= right:
        middle = (left + right) // 2

        if elements[middle] == value:
            return True

        if elements[middle] < value:
            return contains_rec(elements, value, middle + 1, right)
        elif elements[middle] > value:
            return contains_rec(elements, value, left, middle - 1)

    return False

# For scope-related details, this would be a better implementation:
#
# def contains_rec(elements, value):
#     def recursive(left, right):
#         if left <= right:
#             middle = (left + right) // 2
#             if elements[middle] == value:
#                 return True
#             if elements[middle] < value:
#                 return recursive(middle + 1, right)
#             elif elements[middle] > value:
#                 return recursive(left, middle - 1)
#         return False
#     return recursive(0, len(elements) - 1)
