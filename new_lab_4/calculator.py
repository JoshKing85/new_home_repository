'''
Define the function calculator. 
The function will pass three argumets, the first two value and  the third a operator.
Function will calculate the function of the operator on the values passed and return that value.
'''

def calculator(num1, num2, operator):
    
    if operator == "+":
        result = num1 + num2
        print(f"The result is: {result}")

    elif operator =='-':
        result = num1 - num2
        print(f"The result is: {result}")

    elif operator =='*':

        result = num1 *num2
        print(f"The result is: {result}")

    elif operator =='/':
        if num2 == 0:
            print('Error: result is undefined') # As the answer to any fraction with a denominator equal to zero is undefined 
            return                              # an if statement to determine validity of values input is required. If zero the result undefined is output.
             
        else:
            result = num1/num2
            print(f"The result is: {result}")
    
    elif operator =='%':
        if num2 == 0:
            print('Error: result is undefined') # Same execution as previous.
            return                              
             
        else:
            result = num1/num2
            print(f"The result is: {result}")

        result = num1 % num2
        print(f"The result is: {result}")

    elif operator =='>':
        result = num1 > num2
        print(f"The result is: {result}")
    
    elif operator =='>=':
        result = num1 >= num2
        print(f"The result is: {result}")
    
    elif operator =='<':
        result = num1 < num2
        print(f"The result is: {result}")
    
    
    elif operator =='<=':
        result = num1 <= num2
        print(f"The result is: {result}")
    

    else:
        print("Invalid operator.")
        result = False

    return result

# Test values...
calculator(4, 5, "*") # Output: result is: 20
calculator(10, 2, "/") # Output: result is: 5
calculator(4, 0, "/") # Output: Error: result is undefined
calculator(4, 5, "<=") # Output: result is: True
calculator(4, 5, ">") # Output: result is: False
calculator(4, 5, "9") # Output: Invalid operator