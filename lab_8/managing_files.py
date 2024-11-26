import os

def write_to_file(filename, content):
    # complete the function
    with open(filename, 'w') as file:

        file.write(content)


def read_from_file(filename):
    
    # complete the function
    with open( filename, 'r') as file:

        content = file.read()
    return content



def append_to_file(filename, content):
    
    # complete the function
    with open(filename, 'a') as file:

        file.write(content)

def remove_file(filename):
   
   # complete the function
   os.remove(filename)


def count_words(filename, word):
    
    with open(filename, 'r') as f:

        str = f.read()
        str_list = str.split()
        
        count = 0

        for i in str_list:
            if i == word:
                
                count += 1
    return count


def triangle(filename, number):

    with open(filename, 'w') as file:

        count = number
        
        for i in range(number):
            
            new_line = ''
            
            for j in range(count):

                new_line += '*'
            
            
            count -= 1
            if number == count:

                file.write(f'{new_line}')
            else:
                file.write(f'{new_line}\n')
                    
                

            
    with open(filename, 'r') as file:

        tri = file.read()
        print(tri)


