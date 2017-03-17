"""
Nick McLean
"""

def main():
    number_frequency = int(input("frequency? "))
    name = get_name()
    print_loop(name, number_frequency)


def print_loop(name, number_frequency):
    for letter in range(0, len(name), number_frequency):
        print(name[letter])


def get_name():
    name = input("Name? ")
    while name == "":
        print("cannot be blank")
        name = input("Name?: ")
    return name


main()