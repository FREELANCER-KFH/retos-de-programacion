'''
In this project, I created a function that takes a string of words and reverses any word with five or more letters while keeping the order of words and spaces intact. 
It showcases my ability to efficiently manipulate and transform text using Python, making it a simple yet effective solution for text processing tasks.
This project is part of the kata chanllenges in CodeWars for Python beginners.
Att: Kevin Feliz Henríquez.
'''
def spin_words(sentence):
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])

#Test case
sentences = [
    "Hey fellow warriors",
    "This is a test",
    "This is another test"
]

for sentence in sentences:
    print(spin_words(sentence))
