############ GOLD_AOC_STAR #############
GOLD_AOC_STAR = True
############ GOLD_AOC_STAR #############

############## READ_INPUT ##############
with open("--- Day 6: Wait For It ---/input.txt", 'r') as file:
    input = file.read()
############## READ_INPUT ##############

import math
input = input.split("\n")
if GOLD_AOC_STAR:
    times = [int("".join(input[0].split(":")[-1].split()))]
    distances = [int("".join(input[1].split(":")[-1].split()))]
else:
    times = [int(x) for x in input[0].split(":")[-1].split()]
    distances = [int(x) for x in input[1].split(":")[-1].split()]
ways = 1
for i in range(len(times)):
    # -t^2 + t*race_time - record_distance > 0
    lowest_hold = math.ceil((-times[i] + math.sqrt(times[i]**2 - 4*distances[i]))/(-2) + 0.01)
    highest_hold = math.floor((-times[i] - math.sqrt(times[i]**2 - 4*distances[i]))/(-2) - 0.01)
    ways *= highest_hold - lowest_hold + 1
print(ways)