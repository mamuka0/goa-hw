student_info = {  
    "name": "გიორგი",  
    "surname": "მგელი",  
    "academy": "ტექნოლოგიური აკადემია",  
    "fav-color": "მომწვანო",  
    "city": "თბილისი",  
    "goa-student": True,  
    "age": 21,  
    "fav-programming-lang": "პითონი"  
}  

# დაბეჭდვა თითოეული მნიშვნელობა  
for key, value in student_info.items():  
    print(f"{key}: {value}")