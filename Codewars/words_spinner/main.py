'''
In this project, I created a function that takes a string of words and reverses any word with five or more letters while keeping the order of words and spaces intact. 
It showcases my ability to efficiently manipulate and transform text using Python, making it a simple yet effective solution for text processing tasks.
This project is part of the kata chanllenges in CodeWars for Python beginners.
Att: Kevin Feliz Henríquez.
'''
def spin_words(sentence):
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])

#First run
'''

sentences = [
    "Hey fellow warriors",
    "This is a test",
    "This is another test"
]

for sentence in sentences:
    print(spin_words(sentence))
'''

#Test cases
def test_spin_words():
    assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw", "Test 1 Failed"

    assert spin_words("This is a test") == "This is a test", "Test 2 Failed"

    assert spin_words("Hello world") == "olleH world", "Test 3 Failed"

    assert spin_words("This is another test") == "This is rehtona test", "Test 4 Failed"

    assert spin_words("Test") == "Test", "Test 5 Failed"

    assert spin_words("World") == "dlroW", "Test 6 Failed"

    assert spin_words("Python makes coding fun") == "nohtyP sekam gnidoc fun", "Test 7 Failed"

    assert spin_words("Fun fun fun coding coding coding") == "Fun fun fun gnidoc gnidoc gnidoc", "Test 8 Failed"

    assert spin_words("") == "", "Test 9 Failed"

    assert spin_words("Supercalifragilisticexpialidocious") == "suoicodilaipxecitsiligarfilacrepuS", "Test 10 Failed"

    print("All tests passed!")

test_spin_words()
