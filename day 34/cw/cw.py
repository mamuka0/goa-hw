
def remove_elements(main_list, indexes_list):  
  
    for index in indexes_list:  
        if 0 <= index < len(main_list): 
            del main_list[index]  
    print(main_list)  

 
def remove_one_element(my_list, index):  
    if 0 <= index < len(my_list):  
        del my_list[index]  
    print(my_list)  

 
if __name__ == "__main__":  
    main_list = [10, 20, 30, 40, 50]  
    indexes_list = [1, 3]  
    
    print("Original main list:", main_list)  
    remove_elements(main_list, indexes_list)  

    single_list = [1, 2, 3, 4, 5]  
    index_to_remove = 2  
    
    print("Original single list:", single_list)  
    remove_one_element(single_list, index_to_remove)  