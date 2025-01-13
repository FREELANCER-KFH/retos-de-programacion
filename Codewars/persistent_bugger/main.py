'''
In this project, I implements a function to calculate the multiplicative persistence of a number. 
The multiplicative persistence is the number of times the digits of a number must be multiplied together until the result is a single-digit number. 
The function uses a helper to multiply digits iteratively, ensuring an efficient and clear solution.

This project is part of the kata chanllenges in CodeWars for Python.

Att: Kevin Feliz Henríquez.
'''

def persistence(num):
    count = 0
    while num >= 10:
        num = multiply_digits(num)
        count += 1
    return count

def multiply_digits(n):
    result = 1
    while n > 0:
        result *= n % 10  
        n //= 10  
    return result

#It's running time
numbers = [39, 999, 4, 25, 7]

for number in numbers:
    print(f"Input: {number} --> Output: {persistence(number)}")
