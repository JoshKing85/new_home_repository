import numpy as np

def ex1():
    new_list = np.array([])
    for i in range(101):
        
        if i % 6 == 0:
            new_list = np.append(new_list, i)

    total = np.sum(new_list)

    print(total)

def ex2():

    user_input = int(input('Enter number.'  ))

    for i in range(user_input + 1):

        print(i**2)


def ex3():

    count = 2000
    while count < 3000:

        if count % 13 == 0:
            print(f'First number divisible by 13 is {count}.')
            break

        else:
            count += 1 

        if count == 3000:
            print('No number divivisble by 13 between 2000 and 3000')


ex3()



