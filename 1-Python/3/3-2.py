import re

numbers = []
gears = {}

def processLine(lineStr, lineNum):
    for m in re.finditer(r'(\d+)', lineStr):
        numbers.append((int(m.group(0)), m.start(), m.end() - 1, lineNum))

    for m in re.finditer(r'(\*)', lineStr):
        gears[(m.start(), lineNum)] = []

def getPartNumbersNearGears(candidate):
    (val, xs, xe, y) = candidate
    
    for x in range(xs - 1, xe + 2):
        if (x, y - 1) in gears:
            gears[(x, y - 1)].append(val)
        if (x, y + 1) in gears:
            gears[(x, y + 1)].append(val)
    if (xs - 1, y) in gears:
        gears[(xs - 1, y)].append(val)
    if (xe + 1, y) in gears:
        gears[(xe + 1, y)].append(val)

def getRatio(key):
    gear = gears[key]
    if len(gear) == 2:
        return gear[0] * gear[1]
    else:
        return 0

# ~

if __name__ == "__main__":
    sum = 0
    
    file = open('./3.input', 'r')
    for (i, line) in enumerate(file):
        processLine(line, i)

    for number in numbers:
        getPartNumbersNearGears(number)

    for key in gears.keys():
        sum += getRatio(key)

    print(sum)