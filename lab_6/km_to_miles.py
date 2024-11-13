'''
Define function km_to_miles
This function will pass a positive number as kilometers and covert number to miles.
Then return converted value.
'''
def km_to_miles(kilo):

    # Constant conversion as directly proportionate.
    MILE_CON = 0.62

    miles = kilo * MILE_CON 
    miles = round(miles, 3) # Library routine, round()  for decimal required.
    
    return miles

    
'''
Test values 
10, 100, 120
As base 10 increase for first two values, decimal place change expected.
'''

print('Miles traveled are', km_to_miles(10))  # expected outputs: Miles traveled are 6.2
print('Miles traveled are', km_to_miles(100)) # expected outputs: Miles traveled are 62
print('Miles traveled are', km_to_miles(120)) # expected outputs: Miles traveled are 74.4
print('Miles traveled are', km_to_miles(10.32435)) # Test for decimal placement, expected outputs: Miles traveled are 6.401
