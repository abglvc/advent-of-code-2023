############ GOLD_AOC_STAR #############
GOLD_AOC_STAR = True
############ GOLD_AOC_STAR #############

############## READ_INPUT ##############
input = None
with open("--- Day 4: Scratchcards ---/input.txt", 'r') as file:
    input = file.read()
############## READ_INPUT ##############

input = input.split('\n')
instances = [1 for _ in range(len(input))]
res = 0

for i in range(len(input)):
    win_nums, elf_nums = input[i].split(':')[-1].split('|')
    win_nums = [int(num) for num in win_nums.strip().split()]
    elf_nums = [int(num) for num in elf_nums.strip().split()]
    matches = 0
    for wn in win_nums:
        matches += (1 if wn in elf_nums else 0)
    for j in range(matches):
        instances[i+j+1] += instances[i]
    if not GOLD_AOC_STAR and matches != 0: 
        res += 2**(matches-1)

if GOLD_AOC_STAR:
    res = sum(instances)
print(res)