def get_min_power(draws:[]):
    red, green, blue = 0, 0, 0
    for d in draws:
        if d[0] > red:
            red = d[0]
        if d[1] > green:
            green = d[1]
        if d[2] > blue:
            blue = d[2]
    
    return red*green*blue


def possible(game:[], comp):
    for g in game:
        if g[0] > comp[0] or g[1] > comp[1] or g[2] > comp[2]:
            return False

    return True


def extract_draw_details(draw:str):
    red, green, blue = 0, 0, 0
    details = draw.split(",")
    for detail in details:
        detail = detail.strip()
        if "red" in detail:
            red = int(detail[0:detail.find(' ')])
        if "green" in detail:
            green = int(detail[0:detail.find(' ')])
        if "blue" in detail:
            blue = int(detail[0:detail.find(' ')])

    return (red, green, blue)


def extract_draw(line:str):
    colon = line.find(":")
    line = line[colon+2:]
    sections = line.split(";")
    draws = []
    for section in sections:
        section = section.strip()
        tup = extract_draw_details(section)
        draws.append(tup)
    return draws


def get_id(line:str):
    colon = line.find(":")
    space = line.find(" ")
    return int(line[space+1:colon])


#------------------------------------------------------------------------------
print("AoC Day 2")

lines=[]
with open(r"./Input/day2.txt", "r") as input:
    lines = input.readlines()

games = []
for line in lines:
    line = line.strip()
    id = get_id(line)
    draws = extract_draw(line)
    game =[]
    game.append(id)
    game.append(draws)
    games.append(game)

comparison = (12, 13, 14)
total = 0

for game in games:
    if possible(game[1], comparison):
        total += game[0]

print("Total Puzzle 1: ", total)


total = 0

for line in lines:
    line = line.strip()
    draws = extract_draw(line)
    subtotal = get_min_power(draws)
    total += subtotal    

print("Total Puzzle 2: ", total)