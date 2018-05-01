import numpy as np
import math


# upper, lower boundaries, list length
def rand_list(upper, lower, length):

    # generate random list then sort and removes duplicates
    some_list = np.random.randint(upper, lower, length)
    return np.unique(some_list)


# binary search
def binary_search(item, input_list):

    # initialise variables
    item_index = 0
    search_list = input_list

    list_length = len(search_list)

    # loop until 1 item left in list
    while list_length > 1:

        # get mid index (round up)
        mid_index = math.ceil(list_length / 2)

        # if item in first half of list - remove second half of list
        if search_list[mid_index] > item:
            search_list = search_list[:mid_index]

        # if item in second half of list - remove first half of list
        else:
            # adjust the search_list index relative to the input list
            item_index = item_index + mid_index
            search_list = search_list[mid_index:]

        # resize list
        list_length = len(search_list)

    # checks if final item is same as input once 1 item remains
    if input_list[item_index] == item:
        return item_index
    else:
        return -1


# ------ testing below --------

# checks whether the binary search returns the correct item
def check_search(item, search_list):

    index = binary_search(item, search_list)

    if index == -1:
        print(item, ' doesnt exist in list')
    else:
        print('does ', item, ' = ', search_list[index], '?')


# create random list to search and an item to search for
my_list = rand_list(-2000, 2000, 3000)
search_item = 1000

# check it works
check_search(search_item, my_list)