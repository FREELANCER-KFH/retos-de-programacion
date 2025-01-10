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

#It's running time
sneak_case_sentences = [
    "the-stealth-warrior",
    "The_Stealth_Warrior",
    "The_Stealth-Warrior",
    ""
]

for sneak_case_sentence in sneak_case_sentences:
    print(f"Input: {sneak_case_sentences} --> Output: {to_camel_case(sneak_case_sentence)}")
