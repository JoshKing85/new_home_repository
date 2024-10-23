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

    
    
    



winning_list = [1, 2, 3]
user_numbers = [1 , 2, 3]
winning_numbers(user_numbers, winning_list) # Output: 'Congratulations you have won First prize!

winning_list = [1, 2, 3]
user_numbers = [1 , 6, 2]
winning_numbers(user_numbers, winning_list) #Output: 'Congratulations you have won Second prize!

winning_list = [1, 2, 3]
user_numbers = [27, 34, 1]
winning_numbers(user_numbers, winning_list) # Output: 'Congratulations you have won Third prize!

winning_list = [1, 2, 3]
user_numbers = [23, 4, 51]
winning_numbers(user_numbers, winning_list) # Output: 'Congratulations you have won No prize!
