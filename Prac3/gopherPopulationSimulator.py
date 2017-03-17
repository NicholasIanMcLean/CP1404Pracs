"""
Nick McLean
"""
import random

def dead_gopher(population):
    percentage = random.randint(5, 25)
    dead_population = population * (percentage / 100)
    return dead_population

def born_gopher(population):
    percentage = random.randint(10, 20)
    born_population = population * (percentage / 100)
    return born_population

population = 1000
print("Welcome to the Gopher Population Simulator!\nStarting Population: 1000\n")
for year in range(1, 11):
    deadGohper = int(dead_gopher(population))
    bornGohper = int(born_gopher(population))
    population = int(population + bornGohper - deadGohper)
    print("Year {}\n*****\n{} gophers were born. {} died.\nPopulation: {}\n".format(year, bornGohper, deadGohper, population))


