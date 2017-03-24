LOWER = 33
UPPER = 127


def main():
    character = input("Enter a character: ")
    convertedCharacter = ord(character)
    print("The ASCII code for", character, "is", convertedCharacter)

    number = get_number()
    convertedNumber = chr(number)
    print("The ASCII code for", number, "is", convertedNumber)

    for number in range(LOWER, UPPER + 1):
        character = chr(number)
        print("{:3} : {}".format(number, character))


def get_number():
    valid_input = False
    while not valid_input:
        try:
            string_formatted = "Enter a number between {} to {}: ".format(LOWER, UPPER)
            number = int(input(string_formatted))
            while number < LOWER or number > UPPER:
                number = int(input(string_formatted))
            valid_input = True
            return number
        except ValueError:
            print("Invalid (not an integer)")


main()
