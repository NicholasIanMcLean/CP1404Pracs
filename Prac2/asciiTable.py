LOWER = 33
UPPER = 127

character = input("Enter a character: ")
convertedCharacter = ord(character)
print("The ASCII code for", character, "is", convertedCharacter)

stringFormatted = "Enter a number between {} to {}".format(LOWER, UPPER)
number = int(input(stringFormatted))
while number < LOWER or number > UPPER:
    number = int(input(stringFormatted))
convertedNumber = chr(number)
print("The ASCII code for", number, "is", convertedNumber)

number = LOWER
startPoint = LOWER
endPoint = UPPER
while LOWER <= number <= UPPER:
    character = chr(number)
    print("{:3} : {}".format(number, character))
    number += 1