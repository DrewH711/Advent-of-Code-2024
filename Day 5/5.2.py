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

def ordered(book: list):
    allowed = True
    for rule in rules:
        if(rule[0] in book and rule[1] in book):
            a = book.index(rule[0])
            b = book.index(rule[1])
            if(a>b):
                allowed = False
    return allowed
        
def order(book: list):
    sorted = False
    while not sorted:
        for rule in rules:
            if(rule[0] in book and rule[1] in book):
                a = book.index(rule[0])
                b = book.index(rule[1])
                if(a>b):
                    book[a], book[b] = book[b], book[a]
        sorted = ordered(book)
    return book

unorderedlist = []

for book in finput:
    if(not ordered(book)):
        unorderedlist.append(book)

for book in unorderedlist:
    book = order(book)
    length = len(book)
    pagetotal+=book[int((length-1)/2)]

print(pagetotal)