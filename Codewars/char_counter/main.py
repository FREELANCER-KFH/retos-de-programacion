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

'''
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
'''

#test cases:
def test_count_characters():
    assert count_characters("aba") == {'a': 2, 'b': 1}, "Test 1 failed"
    assert count_characters("hello world") == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}, "Test 2 failed"
    assert count_characters("") == {}, "Test 3 failed"
    assert count_characters("abc") == {'a': 1, 'b': 1, 'c': 1}, "Test 4 failed"
    assert count_characters("123123") == {'1': 2, '2': 2, '3': 2}, "Test 5 failed"
    assert count_characters("a!a@b#b$c") == {'a': 2, '!': 1, '@': 1, 'b': 2, '#': 1, '$': 1, 'c': 1}, "Test 6 failed"
    assert count_characters("aaaaabbbbcccdde") == {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}, "Test 7 failed"

    print("All tests passed!")

test_count_characters()
