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



'''
Define the  function is_prime.
This function will pass a postive integer as an argument. The fucntion will test if the integer is prime and return the boolean value.
'''

def is_prime(a):

    prime = False

    if a == 1:
        return prime
    
    else:
        count = 2
        while count < a:
            if a % count == 0:
                break

            else:
                count += 1

    if count == a:
        prime = True

    return prime
    

''' testing values from list are 4, 7, 2, 157.
the expected output are for these values are.
4 is prime? The answer is False
7 is prime? The answer is True
2 is prime? The answer is True
157 is prime? The answer is True
'''
''''
test_values =[4 , 7, 2, 157]

for i in test_values:
    print(f'{i} is prime? The answer is', is_prime(i))

'''

def are_anagrams(first_string, sec_string):
    is_an = True   
    
    if len(first_string) != len(sec_string):
        
        is_an = False
        

    else:
        for i in first_string:
            if i not in sec_string:
                is_an = False
                break
    
    return is_an
        


def caluculate_average(list):

    total = 0
    for i in list:

        total += i
    mean = total / len(list)
    
    return mean



def calculate_weekly_pay(hours):

    if hours <= 35:
        wages = hours*12
        
    
    else:
        over_time = hours - 35
        wages = (35*12) + (over_time*18)
    
    return wages
