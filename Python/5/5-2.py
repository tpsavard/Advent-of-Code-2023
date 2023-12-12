import re

def processSeedLine(s):
    nums = []
    for num in re.findall(r'\d+', s):
        nums.append(int(num))

    seeds = []
    while len(nums) >= 2:
        start = nums.pop(0)
        length = nums.pop(0)
        seeds.append((start, start + length - 1))

    return seeds

def processMapBlock(block):
    mapping = {}
    for i in range(1, len(block)):
        nums = re.findall(r'\d+', block[i])
        origin = int(nums[1])
        adjusted = int(nums[0])
        r = int(nums[2]) - 1
        mapping[(origin, origin + r)] = adjusted - origin
    
    return mapping

def mapSeedRange(seedRange, maps):
    remainingRanges = [seedRange]
    adjustedRanges = []
    for m in maps:
        for (mStart, mEnd) in m.keys():
            covered, notCovered = applyMap(remainingRanges, mStart, mEnd, m[(mStart, mEnd)])
            adjustedRanges += covered
            remainingRanges = notCovered
        remainingRanges += adjustedRanges
        adjustedRanges = []

    m = -1
    for (start, _) in remainingRanges:
        if m == -1 or start < m:
            m = start
    
    return m

def applyMap(seedRanges, mStart, mEnd, adjustment):
    covered = []
    notCovered = []
    for (sStart, sEnd) in seedRanges:
        if sStart > mEnd or mStart > sEnd:
            notCovered.append((sStart, sEnd))
            continue

        cStart = sStart if sStart > mStart else mStart
        cEnd = sEnd if sEnd < mEnd else mEnd
        covered.append((cStart + adjustment, cEnd + adjustment))
        
        if sStart < mStart:
            notCovered.append((sStart, mStart - 1))
        if sEnd > mEnd:
            notCovered.append((mEnd + 1, sEnd))

    return covered, notCovered

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

    adjustedSeeds = []
    for seed in seeds:
       adjustedSeeds.append(mapSeedRange(seed, maps))

    print(min(adjustedSeeds))

