numbers = [x for x in range(1, 11)]  
squares = [x**2 for x in range(1, 6)]  
evens = [x for x in range(1, 21) if x % 2 == 0]  
words = ["apple", "banana", "cherry"]  
first_letters = [word[0] for word in words]  
lower_words = [word.lower() for word in words]  
divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]  
long_words = [word for word in words if len(word) > 4]  
celsius = [0, 10, 20, 30]  
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]  
primes = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]  
sentence = "This is an example sentence for testing"  
long_vowel_words = [word for word in sentence.split() if len(word) > 5 and any(v in word for v in 'aeiou')]  
fibonacci = [0, 1]  
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(18)]