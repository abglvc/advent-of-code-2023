############ GOLD_AOC_STAR #############
GOLD_AOC_STAR = True
############ GOLD_AOC_STAR #############

############## READ_INPUT ##############
with open("--- Day 5: If You Give A Seed A Fertilizer ---/input.txt", 'r') as file:
    input = file.read()
############## READ_INPUT ##############

mappings = []
seeds, maps = input.split("\n\nseed-to-soil map:\n")
seeds = [int(seed) for seed in seeds.split(": ")[-1].split(" ")]
splits = ["\n\nsoil-to-fertilizer map:\n", "\n\nfertilizer-to-water map:\n", "\n\nwater-to-light map:\n",
          "\n\nlight-to-temperature map:\n", "\n\ntemperature-to-humidity map:\n", "\n\nhumidity-to-location map:\n"]
for splt in splits:
    the_map, maps = maps.split(splt)
    mappings.append([[int(y) for y in x.split(" ")] for x in the_map.split("\n")])
mappings.append([[int(y) for y in x.split(" ")] for x in maps.split("\n")])

if GOLD_AOC_STAR:
    seed_ranges = [[seeds[2*i], seeds[2*i] + seeds[2*i+1]-1] for i in range(int(len(seeds)/2))]
else:
    seed_ranges = [[seed, seed+1]for seed in seeds]
new_seed_ranges = []

for map in mappings:
    new_seed_ranges.clear()
    map = sorted(map, key=lambda x: x[1])
    for seed_range in seed_ranges:
        for imap in map:
            imap_range = (imap[1], imap[1]+imap[2]-1)
            if seed_range[0] > imap_range[1]:
                continue
            if seed_range[1] < imap_range[0]:
                break
            lft = max(seed_range[0], imap_range[0])
            rgt = min(seed_range[1], imap_range[1])
            if lft > seed_range[0]:
                new_seed_ranges.append([seed_range[0], lft-1])
                seed_range[0] = lft
            new_seed_ranges.append([imap[0] + lft - imap[1], imap[0] + rgt - imap[1]])
            seed_range[0] = rgt+1
            if seed_range[0] > seed_range[1]:
                break
        if seed_range[0] <= seed_range[1]:
                new_seed_ranges.append(seed_range)
    seed_ranges = new_seed_ranges.copy()

print(sorted(seed_ranges, key=lambda x: x[0])[0][0])