CardValues = {
    "2" => 2, 
    "3" => 3,
    "4" => 4,
    "5" => 5,
    "6" => 6,
    "7" => 7,
    "8" => 8,
    "9" => 9,
    "T" => 10,
    "J" => 11,
    "Q" => 12,
    "K" => 13,
    "A" => 14
}

HandValues = {
    [1, 1, 1, 1, 1] => 1, # High-card
    [2, 1, 1, 1] => 2, # 1 Pair
    [2, 2, 1] => 3, # 2 Pair
    [3, 1, 1] => 4, # 3 of a Kind
    [3, 2] => 5, # Full House
    [4, 1] => 6, # 4 of a Kind
    [5] => 7 # 5 of a Kind
}

# ~

def getHandTypeBV(hand)
    counts = {}
    hand.each_char do |card|
        counts[card] = counts.key?(card) ? counts[card] + 1 : 1
    end
    return HandValues[counts.values.sort.reverse]
end

def compareHands(h1, h2)
    # Sanity Check
    if h2 == nil
        return -1
    end

    # Hand Type Check
    if getHandTypeBV(h1) > getHandTypeBV(h2)
        return -1
    elsif getHandTypeBV(h1) < getHandTypeBV(h2)
        return 1
    end
    
    # Card Values Check
    (0..4).each do |i|
        if CardValues[h1.chars[i]] > CardValues[h2.chars[i]]
            return -1
        elsif CardValues[h1.chars[i]] < CardValues[h2.chars[i]]
            return 1
        end
    end
    
    return -1
end

# ~

hands = []
bets = {}

File.foreach("./7.input") do |line|
    l = line.split(" ")
    hands << l[0]
    bets[l[0]] = l[1]
end

hands.sort! { |h1, h2| compareHands h1, h2 }

sumofbets = 0
count = 1
hands.reverse.each do |hand|
    sumofbets += bets[hand].to_i * count
    count += 1
end

p sumofbets