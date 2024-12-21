rulesdata = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

data = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

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
        length = len(book)
        pagetotal+=book[int((length-1)/2)]

print(pagetotal)