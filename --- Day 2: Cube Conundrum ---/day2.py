############ GOLD_AOC_STAR #############
GOLD_AOC_STAR = True
############ GOLD_AOC_STAR #############

############## READ_INPUT ##############
input = None
with open("--- Day 2: Cube Conundrum ---/input.txt", 'r') as file:
    input = file.read()
############## READ_INPUT ##############

input = input.split('\n')
target_cubes_in_bag = {"red":12, "green":13, "blue":14}
sum = 0

for game_def in input:
    possible = True
    game_info, revealings = game_def.split(':')
    cubes_least = {"red":0, "green":0, "blue":0}
    for reveal in revealings.split(';'):
        for reveal_cubes in reveal.split(','):
            _, cube_amount, cube_color = reveal_cubes.split(' ')
            cube_amount = int(cube_amount)
            if GOLD_AOC_STAR:
                if cube_amount > cubes_least[cube_color]:
                    cubes_least[cube_color] = cube_amount
            elif cube_amount > target_cubes_in_bag[cube_color]:
                possible = False
                break
        if not possible: break
    if possible:
        if GOLD_AOC_STAR:
            sum += cubes_least["red"]*cubes_least["green"]*cubes_least["blue"]
        else:
            sum += int(game_info.split(' ')[-1])
print(sum)