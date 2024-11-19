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
            return 'Undefined'
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
        
        return 'Invalid opereator'

    return result

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

def winning_numbers(user_list, winning_list):


    
    str_list = ['No', 'Third', 'Second', 'First']

    set_list_one = set(user_list)
    set_list_two = set(winning_list)
    total = set.intersection(set_list_one, set_list_two)
    prize = str_list[len(total)]
    if len(total) > 0:
        print(f'Congratulations you have won {prize} prize!')
    else:
        print(f'Unlucky this time you won {prize} prize.')
    
    return prize

def are_anagrams(first_string, sec_string):
     
    
    if len(first_string) != len(sec_string):
        
        is_anagram = False
        
    else:
        
        if sorted(first_string) == sorted(sec_string):
            is_anagram = True
        else:
            is_anagram = False
    
    return is_anagram

def calculate_average(list):

    total = 0
    for i in list:

        total += i
    mean = total / len(list)
    
    return mean

def calculate_weekly_pay(hours):


    if hours <= 35:
        wages = hours*12
    
    else:
        over_time = hours - 35
        wages = (35*12) + (over_time*18)
    
    
    return wages

def sum_of_evens(min_value, max_value):
    
    total = 0
    
    for i in range(min_value, (max_value + 1)):
        if i % 2 ==0:
            print(i)
            total += i
           
    return total


def is_prime(a):


    prime = False

    if a == 1:
        return prime
    
    else:
        count = 2
        while count < a:
            if a % count == 0:
                break

            else:
                count += 1

    if count == a:
        prime = True

    return prime

def celsius_to_fahrenheit(cel):

    #formula for conversion (9/5) * C + 32   
    fahrenheit = ((9/5)*cel) + 32   
    
    return fahrenheit

def decrypt_cypher_text(cypher, key):
    

    new_char = ''
    plain_text = ''
    
    for character in cypher:

        new_char = chr(ord(character)- key)

        plain_text = plain_text + new_char


    return plain_text

def find_maximum_difference(list_1, list_2):

    
    max_diff = 0    

    # Initiate variable for array minumum and maxium values using min() and max() function.
    max_1, max_2, min_1, min_2 = max(list_1), max(list_2), min(list_1), min(list_2)
    
    first_max = max_1 - min_2
    second_max = max_2 - min_1

    if first_max >= second_max:
        max_diff = first_max

    else:
        max_diff = second_max
    
    
    return max_diff

def fuel_cost(miles_travelled):
    # contants for for formula
    MPG = 50
    LITRES = 4.5
    PRICE_PER_LITRE = 1.49

    f_cost = PRICE_PER_LITRE * (miles_travelled / MPG)*LITRES # Formula with constants and variable miles_travelled

    return f_cost

def is_golden_number(n):

    is_gold = False
    
    # Nested loop to find summation of n
    for a in range(n):
        for b in range(n):
            
            # Checks if argument meets all propositional statements.
            if a + b == n and a*b % 1000 == 0:
                is_gold = True
                break
            
                
    return is_gold 

def km_to_miles(kilo):

    # Constant conversion as directly proportionate.
    MILE_CON = 0.62

    miles = kilo * MILE_CON 
    miles = round(miles, 3) # Library routine, round()  for decimal required.
    
    return miles

def letter_occurrence(str):

    # Ordinal for A, a.
    ord_ca, ord_a  = 65, 97
    
    # Set variable to be returned.
    total = 0
    
    for char in str:

        if ord(char) == ord_ca or ord(char) == ord_a:
            
            total += 1

    return total

def annual_net_income(gross):


    net = 0
    # Deductions determined from equal or greater if selections.
    if gross >= 45000:
        net = gross * (1 - 0.5) # All deductions use same formula (1 - n) for percentage reduction.
    
    elif gross >= 30000:
        net = gross * (1 - 0.3)

    else:
        net = gross * (1 - 0.15)
    
    return net

