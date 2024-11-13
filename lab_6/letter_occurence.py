def letter_occurence(str):

    str = str.lower()
    total = 0
    for char in str:

        if char == 'a':

            total += 1

    return total


print('Total number of a\'s is', letter_occurence('amazing'))
