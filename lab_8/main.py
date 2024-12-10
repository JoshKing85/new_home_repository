from managing_files import *
from copy_contents import *
from csv_files import *

if __name__ == "__main__":


    # Create and Write to a file
    write_to_file('temp1.txt', 'copied from temp1.')

    write_to_file('temp2.txt', 'first line of temp2.')

    
    # Append to the file
    #append_to_file('temp.txt', '\nHopefully this is appended to the text file.')
    # Complete your code here...


    # Append to the file
    #append_to_file('temp.txt', '\nand this is a new line')


    #Read from the file
    #read_file = read_from_file('temp.txt')
    #print(read_file)

    #remove_file('temp.txt')

    #Remove the file
    # Complete your code here...
    #word_count = count_words('temp.txt', 'this')
    #print(word_count)

   # triangle('tri.txt', 3)

#     #data = [['Josh', 30, 'male'],
#             ['Jack', 45, 'male'],
#             ['Kenna', 18, 'female'],
#             ['Marie', 40, 'female']]
    
    #create_csv('data_file.csv', data)

    copy_contents()

    