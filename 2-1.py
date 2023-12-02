maxColors = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def validateGame(game):
    rounds = game.split(':')
    gameNum = int(rounds[0].removeprefix('Game '))

    for round in rounds[1].split(';'):
        for color in round.split(','):
            comps = color.strip().split(' ')
            if int(comps[0]) > maxColors[comps[1].lower()]:
                return 0
        
    return gameNum

# ~

if __name__ == "__main__":
    sum = 0
    file = open('./2-1.input', 'r')
    for line in file:
        sum += validateGame(line)

    print(sum)