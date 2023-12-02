import re

def translateStr(digitStr):
    strToDigit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    return strToDigit.get(digitStr) if digitStr in strToDigit else digitStr

sum = 0

file = open('./1-1.input', 'r')
for line in file:
    digits = []
    for match in re.finditer(r"(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))", line):
        digits.append(match.group(1))
    
    if len(digits) < 1:
        continue

    lineVal = int(translateStr(digits[0]) + translateStr(digits[-1]))
    print(lineVal)

    sum += lineVal

print(sum)