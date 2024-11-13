import math

def circle_area(rad):

    area = rad**2 * math.pi
    return area


#print('The area of the circle is:', circle_area(10))

def sum_of_series(n):
    
    sum = 0
    
    for i in range(n):

        sum += i/(i+1)
        print(sum)

    return sum
        

#print(sum_of_series(3))

def cap_convertor(str_to_con):

    str_to_con = list(str_to_con)

    con_str = ''

    for i in range(len(str_to_con)):
      
      ordinate = ord(str_to_con[i])
      new_char = chr(ordinate - 32)
      con_str = con_str + new_char

    return con_str


print(cap_convertor('josh'))
