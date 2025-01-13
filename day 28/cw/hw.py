def manual_index(main_str, search_str):
    
    for i in range(len(main_str) - len(search_str) + 1):
        
        if main_str[i:i+len(search_str)] == search_str:
            return i
   
    return -1
