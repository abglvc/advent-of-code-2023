############ GOLD_AOC_STAR #############
GOLD_AOC_STAR = True
############ GOLD_AOC_STAR #############

############## READ_INPUT ##############
with open("day8/input.txt", 'r') as file:
    input = file.read()
############## READ_INPUT ##############
 
instructions, mapping = input.split("\n\n")
mapping = mapping.split("\n")
network = {}
for map_entry in mapping:
    map_entry = map_entry[:-1]
    node, to_nodes = map_entry.split(" = (")
    network[node] = {"L": to_nodes.split(", ")[0], "R": to_nodes.split(", ")[1]}
 
current_nodes = ["AAA"]
if GOLD_AOC_STAR:
    current_nodes.clear()
    for node in network:
        if node[-1] == "A":
            current_nodes.append(node)

target_steps = []
for current_node in current_nodes:
    step = 0
    while True:
        current_node = network[current_node][instructions[step%len(instructions)]]
        step += 1
        if GOLD_AOC_STAR:
            if current_node[-1] == "Z":
                target = current_node
                break
        else:
            if current_node == "ZZZ":
                break
    if GOLD_AOC_STAR:
        step_target = 0
        while True:
            current_node = network[current_node][instructions[step_target%len(instructions)]]
            step_target += 1
            if current_node == target:
                target_steps.append(step_target)
                break

def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

if GOLD_AOC_STAR:
    for i in range(len(target_steps)-1):
        a = target_steps[i]
        b = target_steps[i+1]
        target_steps[i+1] = a*b/hcf(a,b)
    print(int(target_steps[-1]))
else:
    print(step)