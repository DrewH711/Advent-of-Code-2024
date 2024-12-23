with open("Advent of Code 2024/Day 5/input1.txt") as f:
    rulesdata = f.read()

with open("Advent of Code 2024/Day 5/input2.txt") as f:
    data = f.read()

strinput = data.splitlines()
finput = []

for item in strinput:
    templist=[]
    z = item.split(",")
    finput.append(list(map(int, z)))


temprules = rulesdata.splitlines()
rules = []
for item in temprules:
    x = item.split("|")
    rules.append(tuple(map(int,x)))

print(rules)
pagetotal = 0

for book in finput:
    allowed = True
    bookrules = []

    for rule in rules:
        
        if(rule[0] in book and rule[1] in book):
            # print(f"book: {book}")
            # print(f"rule: {rule}")
            if(book.index(rule[0])>book.index(rule[1])):
                allowed = False
    if(allowed):
        print(book)
        length = len(book)
        pagetotal+=book[int((length-1)/2)]

print(pagetotal)