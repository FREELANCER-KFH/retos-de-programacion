'''
In this project, I developed a solution that remove an espace between two letters.
Then, convert the first letter for each word from the second one, to upper (if and only if that letter is lower.
This project is part of the kata chanllenges in CodeWars for Python beginners.
Att: Kevin Feliz Henríquez.
'''
def to_camel_case(text):
    if not text:
        return ""

    words = text.replace("-", " ").replace("_", " ").split()

    camel_case = words[0] + "".join(word.capitalize() for word in words[1:])
    return camel_case

'''
#It's running time
sneak_case_sentences = [
    "the-stealth-warrior",
    "The_Stealth_Warrior",
    "The_Stealth-Warrior",
    ""
]

for sneak_case_sentence in sneak_case_sentences:
    print(f"Input: {sneak_case_sentences} --> Output: {to_camel_case(sneak_case_sentence)}")
'''

#Test cases:
def test_to_camel_case():
    assert to_camel_case("the-stealth-warrior") == "theStealthWarrior", "Test 1 failed"
    assert to_camel_case("The_Stealth_Warrior") == "TheStealthWarrior", "Test 2 failed"
    assert to_camel_case("The_Stealth-Warrior") == "TheStealthWarrior", "Test 3 failed"
    assert to_camel_case("") == "", "Test 4 failed"
    assert to_camel_case("warrior") == "warrior", "Test 5 failed"
    assert to_camel_case("___") == "", "Test 6 failed"
    assert to_camel_case("stealth-warrior") == "stealthWarrior", "Test 7 failed"
    assert to_camel_case("this_is-a-test-case") == "thisIsATestCase", "Test 8 failed"
    print("All tests passed!")

test_to_camel_case()
