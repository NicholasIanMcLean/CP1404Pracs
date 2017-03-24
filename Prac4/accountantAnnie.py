"""
Nick McLean
"""
income_list = []
number_of_months = int(input("How many months?: "))
total = 0

month_count = 0
while month_count < number_of_months:
    income = float(input("Enter income for month {}: ".format(month_count + 1)))
    income_list.append(income)
    month_count += 1

print("Income Report\n************")
month_count = 0
for i in range(1, number_of_months + 1):
    total += income_list[month_count]
    print("Month {} - Income: ${:10} Total: ${:5}".format(month_count + 1, income_list[month_count], total))
    month_count += 1



