import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
CORV = "cv"


def is_valid_input():
    valid_input = False
    while not valid_input:
        word_format = str.lower(input("word format?: "))
        letter_count = 0

        for letter in word_format:
            if letter in CORV:
                letter_count += 1

        if letter_count == len(word_format):
            valid_input = True
            return word_format
        else:
            print("Invalid format")

word = ""
word_format = is_valid_input()

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)

