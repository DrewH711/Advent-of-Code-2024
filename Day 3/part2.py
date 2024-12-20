import re

file = open("Advent of Code 2024/Day 3/input.txt")
myInput = file.read()
file.close()

expr = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"


def mul(a,b):
    return a*b

x = re.findall(expr, myInput)

go = True
total = 0
print(x)
for expression in x:
    match(expression):
        case "don't()":
            go = False
        case "do()":
            go = True
        case _:
            if(go):
                total += eval(expression)

print(total)