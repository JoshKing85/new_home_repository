'''
Define the function max_of_three.
This function will pass three integers as arguments.
The function will determine the greatest value amongt them and return that value.
'''
def max_of_three(num1, num2, num3):

    if num1 >= num2:

        if num1 >= 3:
            maximum = num1

        else: 
            maximum = num3
    
    else:
        if num2 >= num3:

            maximum = num2
        else:
            maximum = num3

    
    return maximum


#Testing always for maximum of three, therefore all expected outputs are: The maximum value is  3. 
#Test maximums for all postional arguments and repeated values.


maximum = max_of_three(1, 2, 3)
print('The maximum value is ',maximum) 


maximum = max_of_three(3, 2, 1)
print('The maximum value is ',maximum) 

maximum = max_of_three(1, 3, 2)
print('The maximum value is ',maximum) 

maximum = max_of_three(1, 3, 3)
print('The maximum value is ',maximum) #repeated maximum

maximum = max_of_three(2, 2, 3)
print('The maximum value is ',maximum) #repeated non-maximum


maximum = max_of_three(3, 2, 3)
print('The maximum value is ',maximum) # test for repeated value in all positional arguments.

