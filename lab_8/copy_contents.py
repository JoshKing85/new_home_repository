def copy_contents():

    correct_file1 = False
    
    while not correct_file1:
        
        fileone = str(input('Enter filename to be copied.'))
        try:
            with open(fileone, 'r')as f:

                contents = f.read()
                correct_file1 = True
    
        
        except FileNotFoundError:
            
            print(f'{fileone} not found re-enter file name.')
    
        
    
    correct_file2 = False

    while not correct_file2:

        filetwo = str(input('Enter file name to append copied data.'))
        try:
    
            with open(filetwo, 'a') as f:

                f.write('\n' + contents)

    
            with open (filetwo, 'r') as f:

                p_contents = f.read()
                print(p_contents)

                correct_file2 = True

        except FileNotFoundError:
            print(f'{filetwo} not found please re-enter file name.')