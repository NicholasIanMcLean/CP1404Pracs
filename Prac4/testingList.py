"""
Nick McLean
"""

list = []

for i in range(1, 5 + 1):
    number_input = int(input("Number: "))
    list.append(number_input)

print("The first number is ", list[0])
print("The last number is ", list[-1])
print("The smallest number is ", min(list))
print("The largest number is ", max(list))
print("The average number is ", sum(list) / len(list))


