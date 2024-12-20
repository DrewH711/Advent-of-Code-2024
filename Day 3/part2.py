import re

txt = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

#Find all lower case characters alphabetically between "a" and "m":
b = []
x = re.split("""do\(\)""", txt)
length = len(x)
for i in range(length):
    x[i] = x[i].split("don't()")
    n = len(x[i])
    for j in range(n-1):
        if(n%2==0):
            continue
        b = b + re.findall("mul(.+)",x[i][n])
print(b)
print(x)