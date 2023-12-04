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

    return int(2 ** (count - 1) if count > 0 else 0)

# ~

if __name__ == "__main__":
    sum = 0
    
    file = open('./4.input', 'r')
    for line in file:
        sum += processLine(line)

    print(sum)