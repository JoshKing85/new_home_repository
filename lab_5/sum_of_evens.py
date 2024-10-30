import numpy as np


'''

Define function that will,
Pass two arguments, which initialise boundaries. Loop boundary parameters, iterations will extract even value and append to list.
Take sum of array even_list and return cumulative value.

'''
def sum_of_evens(a, b):

    even_list = np.array([])
    for i in range(a, b+1):

        if i % 2 ==0:
            even_list = np.append(even_list, i)

    acc_of_evens = int(np.sum(even_list))

    return acc_of_evens

'''
test value boudaries are set at...

1 to 10
100 to 110
255 to 3355 

expected outputs in order are...

Sum of evens between values 1 and 10 =  30
Sum of evens between values 100 and 110 =  630
Sum of evens between values 255 and 3355 =  2797750

'''
#first values
low_bound, upp_bound = 1, 10
print(f'Sum of evens between values {low_bound} and {upp_bound} = ', sum_of_evens(low_bound, upp_bound))


#second values
low_bound, upp_bound = 100, 110
print(f'Sum of evens between values {low_bound} and {upp_bound} = ', sum_of_evens(low_bound, upp_bound))


#third values
low_bound, upp_bound = 255, 3355
print(f'Sum of evens between values {low_bound} and {upp_bound} = ', sum_of_evens(low_bound, upp_bound))



