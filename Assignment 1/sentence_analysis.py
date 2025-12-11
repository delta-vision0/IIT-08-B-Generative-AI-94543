# Q1: Sentence Analysis
sentence = input("Enter a sentence: ")

num_chars = len(sentence)

num_words = len(sentence.split())

vowels = 'aeiouAEIOU'
num_vowels = 0
for char in sentence:
    if char in vowels:
        num_vowels += 1

print(f"Number of characters: {num_chars}")
print(f"Number of words: {num_words}")
print(f"Number of vowels: {num_vowels}")