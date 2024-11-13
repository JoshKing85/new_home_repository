'''
Define function celsius_to_fahrenheit.
Fucntion will take number as Celsius tempreture and using formula convert to Fahrenheit tempreture.
Then return Fahrenheit tempreture.

'''

def celsius_to_fahrenheit(cel):

    #formula for conversion (9/5) * C + 32   
    fahrenheit = ((9/5)*cel) + 32   
    
    return fahrenheit


'''
Test values...
5, -5, 10, 20
These values will follow simple mathmatical rules, 5, 10 ans 20 will simpifly fraction. -5 will check all for passing a negative value as argument.
Results have basic sum, expected outputs.
'''

print('The tempreture in Fahrenheit is', celsius_to_fahrenheit(5), 'degrees.') # Expected output: The tempreture in Fahrenheit is 41.0 degrees.
print('The tempreture in Fahrenheit is', celsius_to_fahrenheit(-5), 'degrees.') # Expected output: The tempreture in Fahrenheit is 23.0 degrees.
print('The tempreture in Fahrenheit is', celsius_to_fahrenheit(10), 'degrees.') # Expected output: The tempreture in Fahrenheit is 50.0 degrees.
print('The tempreture in Fahrenheit is', celsius_to_fahrenheit(20), 'degrees.') # Expected output: The tempreture in Fahrenheit is 68.0 degrees.