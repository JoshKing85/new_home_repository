'''
Define the  function is_prime.
This function will pass a postive integer as an argument. The function will test if argument is a prime and return a boolean value.

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
    

''' Testing values from list are 4, 7, 2, 157.
Expected outputs for these values are.

True or false, 4 is a prime number? The answer is False
True or false, 7 is a prime number? The answer is True
True or false, 2 is a prime number? The answer is True
True or false, 157 is a prime number? The answer is True

'''

test_values =[4 , 7, 2, 157]

for i in test_values:
    print(f' True or false, {i} is a prime number? The answer is', is_prime(i))
