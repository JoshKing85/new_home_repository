import random

def rock_paper_scissors():
    game_choices = ['rock', 'paper', 'scissors']
    
    outcomes = {('rock', 'rock'): 'boredraw', 
                ('rock', 'paper' ): 'Suck a dick dumbshit you lose! Eternal shame on you and your ancestors. I spit on the day you were born.',
                ('rock', 'scissors') : 'You win. Alright, dont go on about it. You won a silly game I dont even care about. Try to wipe that shot-eating grin off your face.',
                ('paper', 'paper'): 'boredraw',
                ('paper', 'scissors'):'Suck a dick dumbshit you lose! Eternal shame on you and your ancestors. I spit on the day you were born.',
                ('paper', 'rock'): 'You win. Alright, dont go on about it. You won a silly game I dont even care about. Try to wipe that shot-eating grin off your face.',
                ('scissors', 'scissors'): 'boredraw',
                ('scissors', 'rock'):'Suck a dick dumbshit you lose! Eternal shame on you and your ancestors. I spit on the day you were born.',
                ('scissors', 'paper'):'You win. Alright, dont go on about it. You won a silly game I dont even care about. Try to wipe that shot-eating grin off your face.'
               }

    play = True

    while play:
        
        player_choice = input('Enter rock, paper or scissors: ').lower()
        
        if player_choice not in game_choices:
            print(f'Choice "{player_choice}" is not recognized, try again.')
            continue  # Prompt the user again if the choice is invalid


        print(f'You chose {player_choice}.')

        comp_choice = random.choice(game_choices)

        print(f'The computer chose {comp_choice}.')

        print(outcomes[(player_choice, comp_choice)])
        
        play_again = input('want to play again, yes or no? ').lower()
        
        if play_again == 'yes':
            print('Lets do this mother fuckers!')

        else:
            print('Yeah you better run, you dribble of putrid discharge. ')
            break


rock_paper_scissors()