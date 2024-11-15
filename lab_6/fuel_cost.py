'''
Define function fuel_cost.
Function will pass postive number as argument, this value
will represent miles travelled.

Function will use contants and formula to work total price of fuel used,
then return fuel cost.
'''

def fuel_cost(miles_travelled):
    # contants for for formula
    MPG = 50
    LITRES = 4.5
    PRICE_PER_LITRE = 1.49

    f_cost = PRICE_PER_LITRE * (miles_travelled / MPG)*LITRES # Formula with constants and variable miles_travelled

    return f_cost



'''
Test values...

10, 20, 50, 100.

Test will iterate through test values and return expected outcomes...

Fuel cost will be £ 1.341
Fuel cost will be £ 2.682
Fuel cost will be £ 6.705
Fuel cost will be £ 13.41

'''
test_values  = [10, 20, 50, 100]
for i in test_values:
    print('Fuel cost will be £', (fuel_cost(i)))
