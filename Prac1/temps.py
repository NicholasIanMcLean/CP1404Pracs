"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()


def celsius_convert():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def fahrenheit_convert():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)
    print("Result: {:.2f} C".format(celsius))

while choice != "Q":
    if choice == "C":
        celsius_convert()
    elif choice == "F":
        fahrenheit_convert()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")