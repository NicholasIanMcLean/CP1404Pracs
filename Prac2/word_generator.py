import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
CORV = "cv"
word_format = ""

number_in_word_format = int(input("How many letters in the format? "))
for i in range(1, number_in_word_format+1):
    word_format += random.choice(CORV)
print(word_format)

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)