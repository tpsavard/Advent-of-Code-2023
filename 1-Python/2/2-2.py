def calculateGamePower(game):
    rounds = game.split(':')
    # gameNum = int(rounds[0].removeprefix('Game '))

    maxColors = {'red': 0, 'green': 0, 'blue': 0}
    for round in rounds[1].split(';'):
        for color in round.split(','):
            comps = color.strip().split(' ')
            count = int(comps[0])
            name = comps[1].lower()
            if count > maxColors[name]:
                maxColors[name] = count
        
    return maxColors['red'] * maxColors['green'] * maxColors['blue']

# ~

if __name__ == "__main__":
    sum = 0
    file = open('./2-1.input', 'r')
    for line in file:
        sum += calculateGamePower(line)

    print(sum)