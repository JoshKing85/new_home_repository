def golden_number(n):

    is_gold = False

    for a in range(n):
        for b in range(n):

            if a + b == n and a*b % 1000 == 0:
                is_gold = True
            
                
    return is_gold     


is_gold = golden_number(65)

if is_gold is True:

    print('65 is a golden number.')
