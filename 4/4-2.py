import re

def processLine(line):
    nums = line.split(':')[1].split('|')

    winningNums = set()
    for num in re.findall(r'\d+', nums[0]):
        winningNums.add(int(num))

    candidateNums = []
    for num in re.findall(r'\d+', nums[1]):
        candidateNums.append(int(num))
    
    count = 0
    for candidate in candidateNums:
        if candidate in winningNums:
            count += 1

    return count

def getIndexes(start, count):
    indexes = []
    for i in range(1, count + 1):
        indexes.append(start + i)
    return indexes

# ~

if __name__ == "__main__":
    won = {} 
    
    file = open('./4.input', 'r')
    for (i, line) in enumerate(file, 1):
        won[i] = won[i] + 1 if i in won else 1
        indexes = getIndexes(i, processLine(line))
        for index in indexes:
            won[index] = won[index] + won[i] if index in won else won[i]

    print(won)

    sum = 0
    for key in won.keys():
        sum += won[key]

    print(sum)