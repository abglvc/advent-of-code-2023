############ GOLD_AOC_STAR #############
GOLD_AOC_STAR = True
############ GOLD_AOC_STAR #############

############## READ_INPUT ##############
with open("day7/input.txt", 'r') as file:
    input = file.read()
############## READ_INPUT ##############
    

if GOLD_AOC_STAR:
    char_val = { "J":0, "2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, 
            "T":9, "Q":10, "K":11, "A":12 }
else:
    char_val = { "2":0, "3":1, "4":2, "5":3, "6":4, "7":5, "8":6, "9":7, 
                "T":8, "J":9, "Q":10, "K":11, "A":12 }
 
def handStrength(hand):
    vals = []
    for key in char_val:
        vals.append(hand.count(key))
    if GOLD_AOC_STAR:
        joker = vals[0]
        vals[0] = 0
        vals[vals.index(max(vals))] += joker
    type = sum([2**val for val in vals])
 
    value = type**len(hand) + sum([char_val[hand[i]]*(13**((len(hand)-i-1))) for i in range(len(hand))])
    return value
 
input = input.split("\n")
input = sorted(input, key = lambda hand: handStrength(hand.split(" ")[0]))
winnings = sum([(i+1)*int(input[i].split(" ")[-1]) for i in range(len(input))])
print(winnings)