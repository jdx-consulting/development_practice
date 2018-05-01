import numpy as np
import math


# upper, lower boundaries, list length
def rand_list(upper, lower, length):

    # generate random list then sort and removes duplicates
    some_list = np.random.randint(upper, lower, length)
    return np.unique(some_list)


# failed attempt at a binary search using recursive functions - returns none rather than an integer
def binary_search_rec(item, search_list, item_index=0):

    list_length = len(search_list)
    mid_index = math.ceil(list_length/2)

    # checks if end of search has been reached
    if list_length == 1:
        if search_list[0] == item:
            print('I found it! Index: ', item_index)
            return item_index
        else:
            return -1

    # if item in first half of list - remove second half of list
    if search_list[mid_index] > item:
        binary_search_rec(item, search_list[:mid_index], item_index)

    # if item in second half of list - remove first half of list
    else:
        # adjust the search_list index relative to the input list
        item_index = item_index + mid_index
        binary_search_rec(item, search_list[mid_index:], item_index)


# If you run this function you'll see it will print the correct result but will always return None.
# This (I think) is because the return will actually be returning a value to the function that called it,
# which in this case was itself (binary_search_rec) so it seems like I call binary_search_rec,
# which calls binary_search_rec, which calls binary_search_rec........ then binary_search_rec returns a value to the
# binary_search_rec before it and the function basically dies here and returns None.

# Does anyone know to get around this?


# create random list to search and an item to search for
my_list = rand_list(-2000, 2000, 3000)
search_item = 1000

# check it works
binary_search_rec(123, my_list)