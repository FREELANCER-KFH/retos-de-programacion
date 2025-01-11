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

'''
#Running time
sentences = [
    "Pig latin is cool",
    "Hello world !",
    "This is a test, isn't it?",
    "Let's code!"
]

for sentence in sentences:
    print(f"Input: {sentence} --> Output: {pig_it(sentence)}")
'''

#Test cases:
def test_pig_it():
    assert pig_it("Pig latin is cool") == "igPay atinlay siay oolcay", "Test 1 failed"
    assert pig_it("Hello world !") == "elloHay orldway !", "Test 2 failed"
    assert pig_it("This is a test, isn't it?") == "hisTay siay aay esttay, isn'tay itay?", "Test 3 failed"
    assert pig_it("Let's code!") == "et'sLay odecay!", "Test 4 failed"
    assert pig_it("Python") == "ythonPay", "Test 5 failed"
    assert pig_it("!?") == "!?", "Test 6 failed"
    assert pig_it("") == "", "Test 7 failed"

    print("All tests passed!")

test_pig_it()
