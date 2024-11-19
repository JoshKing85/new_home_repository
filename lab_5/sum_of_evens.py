import numpy as np


'''

Define function that will,
Pass two arguments, which initialise boundaries. Loop boundary parameters, iterations will extract even value and append to list.
Take sum of array even_list and return cumulative value.

'''
def sum_of_evens(min_value, max_value):
    
    total = 0
    
    for i in range(min_value, (max_value+ 1)):
        if i % 2 ==0:
            print(i)
            total += i
           
    return total

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
low_bound, upp_bound = 2, 10
print(f'Sum of evens between values {low_bound} and {upp_bound} = ', sum_of_evens(low_bound, upp_bound))

'''
#second values
low_bound, upp_bound = 100, 110
print(f'Sum of evens between values {low_bound} and {upp_bound} = ', sum_of_evens(low_bound, upp_bound))


#third values
low_bound, upp_bound = 255, 3355
print(f'Sum of evens between values {low_bound} and {upp_bound} = ', sum_of_evens(low_bound, upp_bound))
'''


