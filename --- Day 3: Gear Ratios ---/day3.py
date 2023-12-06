############ GOLD_AOC_STAR #############
GOLD_AOC_STAR = True
############ GOLD_AOC_STAR #############

############## READ_INPUT ##############
input = None
with open("--- Day 3: Gear Ratios ---/input.txt", 'r') as file:
    input = file.read()
############## READ_INPUT ##############

input = input.split('\n')
for i in range(len(input)):
    input[i] = [char for char in input[i]]

height = len(input)
width = len(input[0])
sum = 0

def melt_part_number(m, n):
    part_number = 0
    exp = 0
    while (n+1) < len(input[m]) and input[m][n+1].isdigit():
        n += 1
    while n >= 0 and input[m][n].isdigit():
        part_number += (10**exp) * int(input[m][n])
        input[m][n] = "."
        n -= 1; exp += 1
    return part_number

for i in range(height):
    for j in range(width):
        if input[i][j] != '.' and not input[i][j].isdigit():
            if GOLD_AOC_STAR and input[i][j] != "*":
                continue
            num_parts = 0
            ratio = 1
            for m in range(i-1, i+2):
                for n in range(j-1, j+2):
                    try:
                        if input[m][n].isdigit():
                            num_parts += 1
                            if GOLD_AOC_STAR:
                                ratio *= melt_part_number(m, n)
                                continue
                            sum += melt_part_number(m, n)
                    except Exception as e:
                        continue
            if GOLD_AOC_STAR and num_parts == 2:
                sum += ratio
print(sum)