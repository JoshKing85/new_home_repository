import random
def find_maximum_difference(list_1, list_2):

    max_diff = 0

    max_1, max_2, min_1, min_2 = max(list_1), max(list_2), min(list_1), min(list_2)
    

    if max_1 >= max_2:
        max_diff = max_1 - min_2

    else:

        max_diff = max_2 - min_1

    return max_diff




list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]

maxium_difference = find_maximum_difference(list_1, list_2)

print(maxium_difference)




