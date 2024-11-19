'''
Define function find_maximum_difference.
Function will pass two, one dimesional arrays as arguments.
Find the min/max of both arrays, calclate the difference
and return that difference.
'''

def find_maximum_difference(list_1, list_2):

    
    max_diff = 0    

    # Initiate variable for array minumum and maxium values using min() and max() function.
    max_1, max_2, min_1, min_2 = max(list_1), max(list_2), min(list_1), min(list_2)
    
    first_max = max_1 - min_2
    second_max = max_2 - min_1

    if first_max >= second_max:
        max_diff = first_max

    else:
        max_diff = second_max
    
    
    return max_diff
'''
Test values...
arr_1 = [1, 2, 3, 4],
arr_2 = [5, 6, 7, 8],
arr_3 = [234868, 56736848, 580984848, 12754058] test for large numbers,
arr_4 = [1.8678, 5.4847, 23.6867] test for float values.

Test will iterate through test_list, comparing index 0 against remaining elements.
Lowest min value located in arr_1, as min of arr_1 is 1, all max differences should equate to (list max - 1).

Expected outputs:
The Maximum difference is 7
The Maximum difference is 580984847
The Maximum difference is 22.6867
'''
'''
arr_1 = [1, 2, 3, 4]
arr_2 = [5, 6, 7, 8]
arr_3 = [234868, 56736848, 580984848, 12754058]
arr_4 = [1.8678, 5.4847, 23.6867]
test_list = [arr_1, arr_2, arr_3, arr_4]


for i in test_list:
    if i == arr_1:
        continue
    else:
        print('The Maximum difference is', find_maximum_difference(test_list[0], i))
'''
assert find_maximum_difference([11, 12, 11, 12, 0], [11, 11, 11])

print(find_maximum_difference([11, 12, 11, 12, 0], [11, 11, 11]))