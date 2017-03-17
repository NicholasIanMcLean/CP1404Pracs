"""
Nick McLean
"""

name = input("Name? ")
while name == "":
    print("cannot be blank")
    name = input("Name?: ")

for letter in range(1, len(name), 2):
    print(name[letter])