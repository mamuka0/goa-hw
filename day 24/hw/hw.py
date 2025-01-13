
my_list = [1, 2, 3, 4, 5]  
first_element = my_list[0]  
print("პირველი ელემენტი:", first_element)  


last_element = my_list[-1]  
print("ბოლო ელემენტი:", last_element)  


first_three_elements = my_list[:3]  
print("პირველი სამი ელემენტი:", first_three_elements)  

  
my_string = "Hello, World!"  
last_five_characters = my_string[-5:]  
print("ბოლო ხუთი სიმბოლო:", last_five_characters)  

 
reversed_string = my_string[::-1]  
print("გაკვეთა:", reversed_string)  

 
every_third_element = my_list[::3]  
print("ყოველი მესამე ელემენტი:", every_third_element)  

 
half_index = len(my_list) // 2  
first_half = my_list[:half_index]  
second_half = my_list[half_index:]  
print("პირველი ნახევარი:", first_half)  
print("მეორე ნახევარი:", second_half)