'''
In this project, I implement a function that counts the occurrences of each character in a given string. 
The function iterates through the string, using a dictionary to store characters as keys and their counts as values. 
If the string is empty, the function returns an empty dictionary, ensuring edge case handling.

This project is part of the kata chanllenges in CodeWars for Python.

Att: Kevin Feliz Henríquez.
'''
def count_characters(string):
    char_count = {}
    
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

#It's running time
sentences = [
    "aba",
    "hello world",
    "",
    "klk",
    "what's up",
    "aabbcc",
    "123123",
]

for sentence in sentences:
    print(f"Input: '{sentence}' --> Output: {count_characters(sentence)}")
