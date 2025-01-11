def pig_it(text):
    words = text.split()

    transformed_words = [
        word[1:] + word[0] + "ay" if word.isalpha() else word
        for word in words
    ]

    return " ".join(transformed_words)

#Running time
examples = [
    "Pig latin is cool",
    "Hello world !",
    "This is a test, isn't it?",
    "Let's code!"
]

for example in examples:
    print(f"Input: {example} --> Output: {pig_it(example)}")
