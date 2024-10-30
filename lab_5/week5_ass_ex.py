import numpy as np


'''

Define function that will,
Pass two arguments, which will define boundaries. Loop between boudaries, iterations will extract even value and append to list.
Take sum of evens and return accumatlitive value.

'''
def sum_of_evens(a, b):

    even_list = np.array([])
    for i in range(a, b+1):

        if i % 2 ==0:
            even_list = np.append(even_list, i)

    acc_of_evens = np.sum(even_list)

    return acc_of_evens

# Test values for function

#print(sum_of_evens(1, 10))# Expected value 30
#print(sum_of_evens(100, 110))# Expected value 630

def is_prime(a):

    prime = False

    if a == 1:
        return prime
    
    else:
        count = 2
        while count < a:
            if a % count == 0:
                break

    if count == a:
        prime = True

    return prime
    

prime = is_prime(7)
print(prime)  
    
print(6)