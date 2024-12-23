def mix(x,y):
    return x^y
def prune(x):
    return x % 16777216

with open("Advent of Code 2024/Day 22/input.txt") as f:
    rawInput = f.read() 

initialNums = list(map(int, rawInput.splitlines()))

def calc2000(secretNum):
    for i in range(2000):

        step1 = secretNum*64
        secretNum = mix(step1, secretNum)
        secretNum = prune(secretNum)

        step2 = secretNum//32
        secretNum = mix(step2, secretNum)
        secretNum = prune(secretNum)

        step3 = secretNum*2048
        secretNum = mix(step3, secretNum)
        secretNum = prune(secretNum)     

    return secretNum

total = 0
for num in initialNums:
    total += calc2000(num)

print(total)