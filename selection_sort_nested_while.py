arr = [3, 5, 4, 2, 4]

base_pointer = 0







while base_pointer < len(arr) -1:

    low_pointer = base_pointer
    index_pointer = base_pointer

    while index_pointer < len(arr) - 1:

        if arr[index_pointer] > arr[index_pointer + 1]:
            low_pointer = index_pointer + 1
            index_pointer +=1

        else:
            index_pointer += 1

    if low_pointer != base_pointer:
        

        arr[low_pointer], arr[base_pointer], = arr[base_pointer], arr[low_pointer]

    base_pointer += 1

print(arr)
    
        
        


    

    
       
    



