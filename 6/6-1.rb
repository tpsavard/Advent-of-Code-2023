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
contents.first.scan(/\d+/) { |m| times.push m.to_i }
contents.last.scan(/\d+/) { |m| distances.push m.to_i }

product = 1
(0..(times.size - 1)).each do |i| 
    product *= getWinningMoveCount(times[i], distances[i])
end
p product
