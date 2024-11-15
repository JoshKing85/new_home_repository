'''
Define function golden_number.
Function will pass postitive number as argument,
variable is_gold is initialised to Boolean false. Function determines if
sum of the argument can be multiplied to equal the product of 1000.
If propsition is true, is_gold is set to Boolean True.
is_gold is returned.
'''

def golden_number(n):

    is_gold = False
    
    # Nested loop to find summation of n
    for a in range(n):
        for b in range(n):
            
            # Checks if argument meets all propositional statements.
            if a + b == n and a*b % 1000 == 0:
                is_gold = True
                break
            
                
    return is_gold      


'''
Test boundaries...
60 - 100

Test will iterate from 60, as 65 is smallest sum made from multiples of 1000, 
with increments of 5 and determines if iteration is a golden number.

Expected ouputs:
60 is not a golden number.
65 is a golden number.
70 is a golden number.
75 is not a golden number.
80 is not a golden number.
85 is not a golden number.
90 is a golden number.
95 is not a golden number.
100 is not a golden number.
'''

count = 60

while count <= 100:
    
    if golden_number(count):
        print(f'{count} is a golden number.')

        count += 5
    else:
        print(f'{count} is not a golden number.')
        count += 5
