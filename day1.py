def getfirstnumber(line:str):
    for c in line:
        if c.isnumeric():
            return int(c)
        

def getlastnumber(line:str):
    for c in reversed(line):
        if c.isnumeric():
            return int(c)
        

def get_complex_first_num(line:str):
    for i in range(len(line)):
        if line[i].isnumeric():
            return int(line[i])
        else:
            for tup in words:
                if line[i:i+tup[1]] == tup[0]:
                    return tup[2]
                

def get_complex_last_num(line:str):
    revline = my_reverse(line)
    for i in range(len(revline)):
        if revline[i].isnumeric():
            return int(revline[i])
        else:
            for tup in back_words:
                if revline[i:i+tup[1]] == tup[0]:
                    return tup[2]
                

def my_reverse(toreverse:str):
    return toreverse[::-1]

print("AoC Day 1")

words = [ ('one', 3, 1), ('two', 3, 2), ('three', 5, 3), ('four', 4, 4),
          ('five', 4, 5), ('six', 3, 6), ('seven', 5, 7), ('eight', 5, 8),
          ('nine', 4, 9) ]

back_words = [ ('eno', 3, 1), ('owt', 3, 2), ('eerht', 5, 3), ('ruof', 4, 4),
          ('evif', 4, 5), ('xis', 3, 6), ('neves', 5, 7), ('thgie', 5, 8),
          ('enin', 4, 9) ]

lines=[]
with open(r"./Input/day1.txt", "r") as input:
    lines = input.readlines()

total = 0

for l in lines:
    first = int(getfirstnumber(l))
    last = int(getlastnumber(l))
    num = (10*first)+last
    total += num

print("First puzzle solution is ", total)

total = 0

for l in lines:
    tens = get_complex_first_num(l.strip())
    ones = get_complex_last_num(l.strip())
    num = tens*10 + ones
    total += num

print("Second puzzle solution is ", total)