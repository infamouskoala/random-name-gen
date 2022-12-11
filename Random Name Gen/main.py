import random

file = open("names.txt", "r", encoding="utf-8")
reader = file.readlines()
x = list()
for line in reader:
    x.append(line)

name = random.choice(x)
print(name)