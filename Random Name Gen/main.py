import random

file = open("names.txt", "r", encoding="utf-8")
names = file.readlines()

amount = int(input("How many names would you like to generate? "))
for _ in range(amount):
    print(random.choice(names).strip())
