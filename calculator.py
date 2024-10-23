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
            print('Error: result is undefined')
            return
        else:
            result = num1/num2
            print(f"The result is: {result}")
    elif operator =='%':

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

    return result

## Run the example
calculator(4, 5, "*")   # Output: The result is: 20
calculator(10, 2, "/")  # Output: The result is: 5.0
calculator(7, 7, ">=")  # Output: The comparison result is: True
calculator(4, 0, '/')   # Output: The result is undefined.
calculator(8, 5, '<')   # Output: The result is False