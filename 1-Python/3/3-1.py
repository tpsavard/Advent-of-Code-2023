import re

numbers = []
symbols = {}

def processLine(lineStr, lineNum):
    for m in re.finditer(r'(\d+)', lineStr):
        numbers.append((int(m.group(0)), m.start(), m.end() - 1, lineNum))

    for m in re.finditer(r'([^0-9.\n])', lineStr):
        symbols[(m.start(), lineNum)] = m.group(0)

def getValidPartNumbers(candidate):
    (val, xs, xe, y) = candidate
    
    for x in range(xs - 1, xe + 2):
        if (x, y - 1) in symbols:
            return val
        if (x, y + 1) in symbols:
            return val
    if (xs - 1, y) in symbols or (xe + 1, y) in symbols:
        return val

    return 0

# ~

if __name__ == "__main__":
    sum = 0
    
    file = open('./3.input', 'r')
    for (i, line) in enumerate(file):
        processLine(line, i)

    for number in numbers:
        sum += getValidPartNumbers(number)

    print(sum)