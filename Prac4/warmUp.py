numbers = [3, 1, 4, 1, 5, 9 , 2]

print(numbers)

numbers[0] = "ten"
print(numbers)

numbers[-1] = 1
print(numbers)

print(numbers[2:])

check = False
if 9 in numbers:
    check = True
    print(check)