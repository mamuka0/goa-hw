my_tuple = (10, 20, 30, 40, 50)  
second_element = my_tuple[1]  
last_element = my_tuple[-1]  
middle_slice = my_tuple[1:4]  
print(second_element, last_element, middle_slice)



try:  
    my_tuple[1] = 25  
except TypeError as e:  
    print(e)

    my_tuple = (1, 2, 3)  
a, b, c = my_tuple  
print(a, b, c)


my_tuple = (1, 2, 2, 3, 4, 2)  
count_of_twos = my_tuple.count(2)  
index_of_first_two = my_tuple.index(2)  
print(count_of_twos, index_of_first_two)


my_set = {1, 2, 3, 4, 5}  
my_set.add(6)  
my_set.discard(2)  
print(3 in my_set)


set_a = {1, 2, 3}  
set_b = {3, 4, 5}  
union_set = set_a | set_b  
intersection_set = set_a & set_b  
difference_set = set_a - set_b  
print(union_set, intersection_set, difference_set)


my_list = [1, 2, 2, 3, 4, 4, 5]  
my_set = set(my_list)  
unique_list = list(my_set)  
print(unique_list)