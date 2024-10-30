'''
Define the function are_anagrams.
This function will pass two strings as arguments. The function will validate length and alpha mirroring.
The funtion will then return a boolean value.

'''

def are_anagrams(first_string, sec_string):
    is_anagram = True   
    
    if len(first_string) != len(sec_string):
        
        is_anagram = False
        

    else:
        for i in first_string:
            if i not in sec_string:
                is_anagram = False
                break
    
    return is_anagram
'''
Testing pairs are...

right, grith
wrong, groown 
error, rarer

expected outputs...

right and grith are anagrams.
wrong and groown are not anagrams.
error and rarer are not anagrams.

'''
# 1st pair
if are_anagrams('right', 'grith'):
    print('right and grith are anagrams.')

else:
    print('right and grith are not anagrams.')


# 2nd pair
if are_anagrams('wrong', 'groown'):
    print('wrong and groown are anagrams.')

else:
    print('wrong and groown are not anagrams.')


# 3rd pair 
if are_anagrams('error', 'rarer'):
    print('error and rarer are anagrams.')

else:
    print('error and rarer are not anagrams.')
