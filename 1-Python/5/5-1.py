import re

def processSeedLine(s):
    seeds = []
    for num in re.findall(r'\d+', s):
        seeds.append(int(num))

    print(seeds)
    return seeds

def processMapBlock(block):
    mapping = {}
    for i in range(1, len(block)):
        nums = re.findall(r'\d+', block[i])
        original = int(nums[1])
        adjusted = int(nums[0])
        r = int(nums[2]) - 1
        mapping[(original, original + r)] = adjusted
    
    print(mapping)
    return mapping

def mapSeedValue(seed, maps):
    adjusted = seed
    for m in maps:
        for (start, end) in m.keys():
            if adjusted >= start and adjusted <= end:
                adjusted = m[(start, end)] + (adjusted - start)
                break

    print(str(seed) + " -> " + str(adjusted))
    return adjusted

# ~

if __name__ == "__main__":
    blocks = []
    
    file = open('./5.input', 'r')
    curBlock = []
    for line in file:
        if line == "\n":
            blocks.append(curBlock)
            curBlock = []
        else:
            curBlock.append(line)
    blocks.append(curBlock)

    seeds = processSeedLine(blocks[0][0])
    maps = []
    for i in range(1, len(blocks)):
        maps.append(processMapBlock(blocks[i]))

    mappedSeeds = []
    for seed in seeds:
        mappedSeeds.append(mapSeedValue(seed, maps))

    print(min(mappedSeeds))