import numpy as np
import math


def herons_formula():

    user_first_len = float(input('Enter first length. '))
    user_sec_len = float(input('Enter second length. ' ))
    user_third_len = float(input('Enter third length '))

    s =     (user_first_len + user_sec_len + user_third_len)/2

    area = math.sqrt(s*(s-user_first_len)*(s-user_sec_len)*(s-user_third_len))

    return area

#print(herons_formula())


def odometer_sting():

    data_val = False

    while not data_val:

        user_input = input('Enter all 6 numbers from odometer. ')
        correct_input = input(f'You entered {user_input}, enter yes if this is the correct reading. ')

        if correct_input == 'yes':

            try:
                user_int = int(user_input)

                if len(user_input) == 6:
                    data_val = True
                
                else:
                    raise ValueError(print(' 6 numbers are required for an accurate reading.'))
                
            except ValueError:
                print('Enter only numbers.')

    user_input_list = list(user_input)

    for i in range(len(user_input_list)):
        int_char = int(user_input_list[i])

        if int_char > 5:
            int_char -= 1
            user_input_list[i] = str(int_char)

        
        user_input = ''.join(user_input_list)
    return user_input
                    
                
print(f'Your updated reading is {odometer_sting()}.')        
                    
            
                


        

       
