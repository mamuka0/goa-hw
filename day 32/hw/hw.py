# 3
def welcome_message(name, age):  
    return f"Welcome {name}! You are {age} years old."  

# 4
def format_name(first_name, last_name):  
    return f"{first_name.capitalize()} {last_name.capitalize()}"  

# 5
def reverse_string(s):  
    reversed_s = s[::-1]  
    return f"The reversed string is: {reversed_s}"  

# 6
def insert_word(sentence, word, index):  
    words = sentence.split()  
    words.insert(index, word)  
    return ' '.join(words)  

# 7 
def sentence_to_words(sentence):  
    return sentence.split()  

# 8
def csv_to_list(csv_string):  
    return csv_string.split(',')  

# 9
def split_paragraph(paragraph):  
    return paragraph.split('. ')


    my_list = [1, 2, 3]  
print(append_item(my_list, 4))  

my_list = [1, 2, 3]  
print(append_multiple_items(my_list, [4, 5, 6]))  

list1 = [1, 2]  
list2 = [3, 4]  
print(append_list_to_list(list1, list2))  

print(insert_item_at(my_list, 1, 10))  

my_list = [1, 2, 3]  
print(insert_at_beginning(my_list, 0)) 

my_list = [1, 2, 3]  
print(insert_at_end(my_list, 4)) 