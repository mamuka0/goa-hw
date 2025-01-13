# # Taking three numbers as input  
# num1 = float(input("Enter first number: "))  
# num2 = float(input("Enter second number: "))  
# num3 = float(input("Enter third number: "))  

# # Finding the largest number  
# largest = max(num1, num2, num3)  

# # Printing the largest number  
# print(f"The largest number is: {largest}")


# # Taking score as input  
# score = float(input("Enter the score (0-100): "))  

# # Determining the grade based on the score  
# if 90 <= score <= 100:  
#     grade = 'A'  
# elif 80 <= score < 90:  
#     grade = 'B'  
# elif 70 <= score < 80:  
#     grade = 'C'  
# elif 60 <= score < 70:  
#     grade = 'D'  
# elif score < 60:  
#     grade = 'F'  
# else:  
#     grade = 'Invalid score'  

# # Printing the grade  
# print(f"The grade is: {grade}")


# # Taking a number as input  
# number = float(input("Enter a number: "))  

# # Checking if the number is positive, negative, or zero  
# if number > 0:  
#     print("The number is positive.")  
# elif number < 0:  
#     print("The number is negative.")  
# else:  
#     print("The number is zero.")


# # Taking two integers as input  
# start = int(input("Enter the starting integer: "))  
# end = int(input("Enter the ending integer: "))  

# # Calculating the sum of numbers between start and end  
# total_sum = 0  

# for i in range(start, end + 1):  
#     total_sum += i  

# # Printing the sum  
# print(f"The sum of numbers between {start} and {end} is: {total_sum}")

# Taking a number as input  
num = int(input("Enter a number: "))  

# # Function to check if a number is prime  
# def is_prime(n):  
#     if n <= 1:  
#         return False  
#     for i in range(2, int(n ** 0.5) + 1):  
#         if n % i == 0:  
#             return False  
#     return True  

# # Checking if the number is prime  
# if is_prime(num):  
#     print(f"{num} is a prime number.")  
# else:  
#     print(f"{num} is not a prime number.")


# # Creating a list of five numbers  
# numbers = [10, 20, 30, 40, 50]  

# # Printing the first, third, and last elements using indexing  
# print("First element:", numbers[0])  
# print("Third element:", numbers[2])  
# print("Last element:", numbers[-1])


# # Creating a list of 20 elements of various data types  
# elements = [1, "two", 3.0, True, None, "six", 7, 8.5, "nine", 10,   
#             [11, 12], (13, 14), {15: "fifteen"}, {16, 17}, "eighteen", 19,   
#             20, 21.5, False, "lastElement"]  

# # Printing all the elements using indexing  
# for index in range(len(elements)):  
#     print(f"Element at index {index}: {elements[index]}")


