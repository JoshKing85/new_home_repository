'''
Define function calculate_average.
Pass an array of numbers as an argument,
calculate the mean avarage of the array and return that value.

'''
def caluculate_average(list):

    total = 0
    for i in list:

        total += i
    mean = total / len(list)
    
    return mean


'''
test arrays are..

arr1 = 1, 3, 4, 5
arr2 = 3.6, 4.3, 2.6, 8.2, 1.4
arr3 = 2*4, 23/12, 3**5, 45%3, 35/6
arr4 = arr1 + arr2

expected outputs in order of loop interations, for array test_values...

The mean value in arr 1  =  3.8
The mean value in arr 2  =  4.02
The mean value in arr 3  =  51.95
The mean value in arr 4  =  3.91

'''
arr1 = [1, 3, 4, 5, 6]
arr2 = [3.6, 4.3, 2.6, 8.2, 1.4]
arr3 = [2*4, 23/12, 3**5, 45%4, 35/6]
arr4 = arr1 + arr2 # [1, 3, 4, 5, 6, 3.6, 4.3, 2.6, 8.2, 1.4]

test_values = [arr1, arr2, arr3, arr4]

for i in range(4):
    print('The mean value of the sum of arr',i + 1, ' = ', caluculate_average(test_values[i]))

print(arr3)

