'''
In this project, I implement a function to convert a sentence into "Pig Latin". 
The transformation involves moving the first letter of each word to the end and appending "ay" to it, leaving punctuation untouched. 
The function handles both simple and complex sentences, demonstrating efficient string manipulation and condition handling.

This project is part of the kata chanllenges in CodeWars for Python.

Att: Kevin Feliz Henríquez.
'''

def pig_it(text):
    words = text.split()

    transformed_words = [
        word[1:] + word[0] + "ay" if word.isalpha() else word
        for word in words
    ]

    return " ".join(transformed_words)

#Running time
sentences = [
    "Pig latin is cool",
    "Hello world !",
    "This is a test, isn't it?",
    "Let's code!"
]

for sentence in sentences:
    print(f"Input: {sentence} --> Output: {pig_it(sentence)}")
