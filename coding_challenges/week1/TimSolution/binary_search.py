import math


def binary_search(find_element, my_list):

    upper = len(my_list) - 1    # zero-indexed
    lower = 0

    while True:    # Create loop. Perhaps risky, but provided my logic is sound, should be fine.
        midpoint = math.floor((upper + lower) / 2)  # floor() to round down. Could equally use ciel()
        mid_element = my_list[midpoint]
        if mid_element == find_element:
            return midpoint
        elif mid_element > find_element:
            upper = midpoint - 1    # if found element found is above the sought element, update the upper bound
        else:
            lower = midpoint + 1    # otherwise, update the lower bound
        if upper < lower:
            return -1   # once the above process has been through the maximum iterations, the update will make
                        # upper = lower - 1, so should terminate and conclude not in list.


test_list = [1, 2, 3, 5, 8, 13, 21, 34, 55]    # initialise ordered list
print('Your ordered list is: ', test_list)
test_element = float(input('What number are you trying to find?: '))   # request number to find, convert to float
print(binary_search(test_element, test_list))
