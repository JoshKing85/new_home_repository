duplicate_list = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicates(list_to_remove):
    set_one = set(list_to_remove)
    print(set_one)
    
    ret_list = list(set_one)
    return ret_list


print(remove_duplicates(duplicate_list))