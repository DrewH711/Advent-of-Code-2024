f = open("Advent of Code 2024/Day 4/input.txt")
input = f.read()
f.close()

temp = input.splitlines()

newinput = []
for item in temp:
    newinput.append(list(item))

rows = len(newinput)
columns = len(newinput[0])
print(f"rows: {rows}, columns: {columns}")
print(newinput)

xmasCounter = 0
# a row can be referenced using newinput[x], and a column using newinput[0][y]
# if X is found, check next letters in this order: top left, middle left, bottom left, etc. continuing counterclockwise

for row in range(rows): 
    for column in range(columns):
        relCoords = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            ### THIS IS IN THE FORMAT (Y,X), WHERE 0,0 IS THE TOP LEFT
        if(newinput[row][column]=="X"):
            for coord in relCoords:
                y = coord[0]
                x = coord[1]

                
                inBounds = True
                try:
                    testCoords = [newinput[row+y][column+x],newinput[row+(2*y)][column+(2*x)],newinput[row+(3*y)][column+(3*x)]]
                    if(testCoords[0]=="M" and testCoords[1]=="A" and testCoords[2]=="S"):
                        if(row+(3*y)<0 or column+(3*x)<0):
                                inBounds = False
                        if(inBounds):
                            # print(f"X found at ({row, column}), M found at ({row+y, column+x}), A found at ({row+(2*y),column+(2*x)}), S found at ({row+(3*y),column+(3*x)})")
                            xmasCounter+=1
                except IndexError:
                    continue


"""        ### THIS DOES NOT WORK DUE TO INDEX ERRORS THAT IDK HOW TO HANDLE

        if(newinput[row][column]=="X"):
            #check top left relative to current position
            
            if(newinput[row-1][column-1]=="M" and newinput[row-2][column-2]=="A" and newinput[row-3][column-3]=="S"):
                xmasCounter+=1
            #check relative immediate left 
            if(newinput[row][column-1]=="M" and newinput[row][column-2]=="A" and newinput[row][column-3]=="S"):
                xmasCounter+=1
            #check bottom left
            if(newinput[row+1][column-1]=="M" and newinput[row+2][column-2]=="A" and newinput[row+3][column-3]=="S"):
                xmasCounter+=1
            #check straight down
            if(newinput[row+1][column]=="M" and newinput[row+2][column]=="A" and newinput[row+3][column]=="S"):
                xmasCounter+=1
            #check bottom right
            if(newinput[row+1][column+1]=="M" and newinput[row+2][column+2]=="A" and newinput[row+3][column+3]=="S"):
                xmasCounter+=1
            #check immediate right
            if(newinput[row][column+1]=="M" and newinput[row][column+2]=="A" and newinput[row][column+3]=="S"):
                xmasCounter+=1   
            #check top right        
            if(newinput[row-1][column+1]=="M" and newinput[row-2][column+2]=="A" and newinput[row-3][column+3]=="S"):
                xmasCounter+=1
            #check straight up
            if(newinput[row-1][column+1]=="M" and newinput[row-2][column+2]=="A" and newinput[row-3][column+3]=="S"):
                xmasCounter+=1"""

print(xmasCounter)