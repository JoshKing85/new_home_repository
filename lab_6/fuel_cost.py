def fuel_cost(miles_traveled):

    MPG = 50
    LITRES = 4.5
    PRICE_PER_LITRE = 1.49

    f_cost = PRICE_PER_LITRE * (miles_traveled / MPG)*LITRES

    return f_cost
f_cost = fuel_cost(50)
print('The cost of fuel for 50 miles is £' + str(f_cost))

