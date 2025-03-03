# 1. შექმენით dictionary  
student_info = {  
    "name": "გიორგი",  
    "surname": "მგელი",  
    "academy": "ტექნოლოგიური აკადემია",  
    "fav-color": "მომწვანო",  
    "city": "თბილისი",  
    "goa-student": True,  
    "age": 21,  
    "fav-programming-lang": "პითონი",  
    "hobby": "კითხვა",  
    "favorite-food": "ხაჭაპური"  
}  

# 2. გასაღების დაბეჭდვა  
keys = student_info.keys()  
print("Keys:", keys)  

# 3. მნიშვნელობების დაბეჭდვა  
values = student_info.values()  
print("Values:", values)  

# 4. გასაღების და მნიშვნელობების დაბეჭდვა  
items = student_info.items()  
print("Items:")  
for key, value in items:  
    print(f"{key}: {value}")  

# 5. წრებაზე განხორციელება  
print("Iterating through items:")  
for key, value in student_info.items():  
    print(f"{key}: {value}")  

# 6. კონტროლი, თუ გასაღები არსებობს  
key_to_check = "age"  
if key_to_check in student_info:  
    print(f"{key_to_check} exists")  
else:  
    print(f"{key_to_check} does not exist")  

# 7. მნიშვნელობის მიღება get() მეთოდის გამოყენებით  
age = student_info.get("age", "Key does not exist")  
print("Age:", age)  

# 8. ახალი გასაღების მიწერა  
student_info["grade"] = "A"  
print("Updated Dictionary:", student_info)  

# 9. გასაღების წაშლა  
student_info.pop("hobby")  
print("Updated Dictionary after pop:", student_info)  

# 10. სხვა dictionary-ს გამოყენებით განახლება  
other_info = {"year": 2023, "major": "ინფორმატიკა"}  
student_info.update(other_info)  
print("Dictionary after update:", student_info)  

# 11. dictionary-ის სიგრძის დაბეჭდვა  
length = len(student_info)  
print("Length of dictionary:", length)  

# 12. ჯამი ყველა ნუმერულ მნიშვნელობაზე  
def sum_numeric_values(dictionary):  
    return sum(value for value in dictionary.values() if isinstance(value, (int, float)))  

numeric_sum = sum_numeric_values(student_info)  
print("Sum of numeric values:", numeric_sum)  

# 13. ყველა ელემენტის მიღება  
student_info.clear()  
print("Dictionary after clear:", student_info)  

# 14. ინფორმაცია თქვენი შესახებ  
another_student_info = {  
    "name": "ნიკა",  
    "surname": "ბექაძე",  
    "academy": "უნივერსიტეტი",  
    "fav-color": "შავი",  
    "city": "ბათუმი",  
    "goa-student": False,  
    "age": 22,  
    "fav-programming-lang": "ჯავასკრიპტი",  
    "hobby": "მუსიკა",  
    "favorite-food": "ჰამბურგერი"  
}  

print("Another Student Info:", another_student_info)