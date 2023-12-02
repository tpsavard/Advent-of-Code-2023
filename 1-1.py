import re

sum = 0

file = open('./1-1.input', 'r')
for line in file:
    digits = re.findall(r"[0-9]{1}", line)
    
    if len(digits) < 1:
        continue

    firstDigit = digits[0]
    lastDigit = digits[-1]
    lineVal = int(firstDigit + lastDigit)
    print(lineVal)

    sum += lineVal

print(sum)