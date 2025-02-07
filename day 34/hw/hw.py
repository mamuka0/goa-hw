 
def print_hello():  
    print("Hello, World!")  

 
def print_sum(num1, num2):  
    print(num1 + num2)  


def multiply_by_ten(number):  
    return number * 10  


def greet(name="Guest"):  
    print(f"Hello, {name}!")  

 
def outer_function():  
    def inner_function():  
        print("This is the inner function.")  
    inner_function()  

 
def check_even_odd(numbers):  
    for number in numbers:  
        if number % 2 == 0:  
            print("Even")  
        else:  
            print("Odd")  


def find_max(numbers):  
    max_number = numbers[0]  
    for number in numbers:  
        if number > max_number:  
            max_number = number  
    return max_number  

  
def filter_positive(numbers):  
    positive_numbers = []  
    for number in numbers:  
        if number > 0:  
            positive_numbers.append(number)  
    return positive_numbers  

 
def sum_divisible_by_three():  
    total_sum = 0  
    for number in range(1, 101):  
        if number % 3 == 0:  
            total_sum += number  
    return total_sum  


if __name__ == "__main__":  
    print_hello()  
    print_sum(5, 10)   
    print(multiply_by_ten(5))  
    greet()  
    greet("Alice")   
    outer_function()   
    
    check_even_odd([1, 2, 3, 4, 5])
    
    numbers_list = [3, 5, 2, 8, -1]  
    print(find_max(numbers_list)) 
    
    int_list = [3, -2, 7, 0, -1, 4]  
    print(filter_positive(int_list))   

    print(sum_divisible_by_three())  