def getNext(seq) 
    deriv = [] << seq
    
    cur = seq 
    while ! checkSeq(cur)
        cur = getDerivSeq(cur)
        deriv << cur
    end
    # p deriv

    firsts = [0]
    (deriv.size - 2).downto(0).each do |i|
        firsts << deriv[i].first - firsts.last
    end
    # p firsts
    
    return firsts.last
end

def checkSeq(seq)
    seq.each { |i| return false if i != 0 }
    return true
end

def getDerivSeq(seq)
    return [0] if seq.size < 2

    deriv = []
    (1..(seq.size - 1)).each do |i|
        deriv << (seq[i] - seq[i - 1])
    end
    return deriv
end

# ~

sum = 0
File.foreach("./9.input") do |line|
    sum += getNext(line.scan(/-?\d+/).map { |s| s.to_i })
end
p sum