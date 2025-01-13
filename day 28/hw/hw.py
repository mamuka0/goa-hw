def manual_index(main_string, search_string):  
    
    main_length = len(main_string)  
  
    search_length = len(search_string)  

    
    if search_length == 0:  
        return 0 
    
    for i in range(main_length - search_length + 1):  
          
        if main_string[i:i + search_length] == search_string:  
            return i   
            
    return -1  

 
main_string = "გამარჯობა, ეს არის ჩემი ტექსტი."  
search_string = "ჩემი"  
index = manual_index(main_string, search_string)  

print(f"'{search_string}' ინდექსი '{main_string}'-ში არის: {index}")