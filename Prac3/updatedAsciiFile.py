LOWER = 33
UPPER = 127

get_number()
convertedNumber = chr(number)
print("The ASCII code for", number, "is", convertedNumber)

def get_number():
    global number
    try:
        string_formatted = "Enter a number between {} to {}: ".format(LOWER, UPPER)
        number = int(input(string_formatted))
        while number < LOWER or number > UPPER:
            number = int(input(string_formatted))
        return number
    except ValueError:
        print("try again")



