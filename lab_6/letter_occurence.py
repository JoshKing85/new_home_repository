'''
Define function letter_occurance.
Function will pass string as an argument then calculate occurances of characters A, a.
As no built-in-routines allowed, function will use ordinals for comparison.
Then return total occurances.
'''

def letter_occurence(str):

    # Ordinal for A, a.
    ord_ca, ord_a  = 65, 97
    
    # Set variable to be returned.
    total = 0
    
    for char in str:

        if ord(char) == ord_ca or ord(char) == ord_a:
            
            total += 1

    return total

'''
Test values...
amazing, PAss an ArbiTrary pHrase as arguMent,
not it this one.

Will test for single word, sentence with both upper and lower characters, and a zero value.
'''

print('Total number of a\'s are', letter_occurence('amazing')) # Expected output: Total number of a\'s are 2
print('Total number of a\'s are', letter_occurence('PAss an ArbiTrary pHrase as arguMent')) # Expected output: Total number of a\'s are 7
print('Total number of a\'s are', letter_occurence('not it this one')) # Expected output: Total number of a\'s are 0
