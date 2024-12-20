f = open("Advent of Code 2024/Day 4/input.txt")
input = f.read()
f.close()

temp = input.splitlines()

newinput = []
for item in temp:
    newinput.append(list(item))



rows = len(newinput)
columns = len(newinput[0])

xmasCounter = 0


for row in range(rows): 
    for column in range(columns):
        check1 = False
        check2 = False
        if(newinput[row][column]=="A"):
            try:
                match(newinput[row-1][column+1]): #check upper right corner relative to A
                    case "M":
                        if(newinput[row+1][column-1]=="S"): #check that opposite corner contains S or M depending on which is found in upper right
                            check1 = row>0 and rows>row and column>0 and columns>column #make sure the A isn't on an edge
                    case "S":
                        if(newinput[row+1][column-1]=="M"):
                            check1 = row>0 and rows>row and column>0 and columns>column
                    case _:
                        continue

                match(newinput[row-1][column-1]): #same thing on the other side
                    case "M":
                        if(newinput[row+1][column+1]=="S"):
                            check2 = row>0 and rows>row and column>0 and columns>column
                    case "S":
                        if(newinput[row+1][column+1]=="M"):
                            check2 = row>0 and rows>row and column>0 and columns>column
                    case _:
                        continue
                if(check1 and check2):
                    xmasCounter+=1
            except IndexError:
                continue
print(xmasCounter)
"""
S . S   S . M
. A .   . A .
M . M   S . M
"""
