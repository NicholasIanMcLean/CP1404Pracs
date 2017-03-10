try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Value error runs when something is entered as a letter/symbol when it is expecting a numerical value
#zeroDivision runs when something is trying to be divided by 0
# error check inputs for not being 0?