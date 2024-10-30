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



maximum = max_of_three(1, 2, 3)
print(maximum) # outcome 3 should be printed.


maximum = max_of_three(3, 2 ,1)
print(maximum)

maximum =  max_of_three(1,3,2)
print(maximum)

maximum =  max_of_three(1, 3, 3)
print(maximum)

maximum =  max_of_three(3, 1, 3)
print(maximum)

maximum =  max_of_three(3, 3 , 1)
print(maximum)