def fixNumbers(numbers)
    str = ""
    numbers.each { |number| str += number } 
    return str.to_i
end

def getWinningMoveCount(time, bestDistance)
    wins = 0
    (0..time).each do |speed|
        distance = speed * (time - speed)
        wins += 1 if distance > bestDistance
    end    
    p wins
end

# ~

times = Array.new
distances = Array.new

contents = File.read("./6.input").split("\n")
contents.first.scan(/\d+/) { |m| times.push m }
contents.last.scan(/\d+/) { |m| distances.push m }

p getWinningMoveCount(fixNumbers(times), fixNumbers(distances))
