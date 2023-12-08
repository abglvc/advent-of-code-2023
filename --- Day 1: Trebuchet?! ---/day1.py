############ GOLD_AOC_STAR #############
GOLD_AOC_STAR = True
############ GOLD_AOC_STAR #############

############## READ_INPUT ##############
with open("--- Day 1: Trebuchet?! ---/input.txt", 'r') as file:
    input = file.read()
############## READ_INPUT ##############

input = input.split('\n')
digits_string = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0

for line in input:
    first = None
    last = None
    min = len(line)
    max = -1
    if GOLD_AOC_STAR:
        for i in range(len(digits_string)):
            lindex = line.find(digits_string[i])
            rindex = line.rfind(digits_string[i])
            if lindex != -1 and lindex < min:
                min = lindex
                first = i+1
            if rindex > max:
                max = rindex
                last = i+1
    for i in range(len(line)):
        if line[i].isdigit():
            if i < min:
                first = int(line[i])
                min = i
            if i > max:
                last = int(line[i])
                max = i
    if (last == None):
        last = first
    sum += first*10 + last
print(sum)