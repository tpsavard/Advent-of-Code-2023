def processInstructionLine(line, instructions)
    line.chars.each do |c|
        case c
        when "L"
            instructions << :left
        when "R"
            instructions << :right
        else
            next
        end
    end
end

def processMapLine(line, map, startingNodes, endingNodes)
    md = /([0-9A-Z]{3}) \= \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)/.match line
    map[md.captures[0]] = { left: md.captures[1], right: md.captures[2] }

    startingNodes << md.captures[0] if /..A/.match? md.captures[0]
    endingNodes << md.captures[0] if /..Z/.match? md.captures[0]
end

def walkTheMap(instructions, map, startingNode, endingNodes)
    steps = 0
    cur = startingNode
    while ! endingNodes.include? cur
        options = map[cur]
        cur = options[instructions[steps % instructions.size]]
        steps += 1
    end
    return steps
end

def getLcm(ints)
    return 0 if ints.size < 1
    return ints[0] if ints.size == 1

    cur = ints[0].lcm(ints[1])
    ints[2, ints.size - 1].each { |int| cur = cur.lcm(int)}
    return cur
end

# ~

instructions = []
map = {}
startingNodes = []
endingNodes = []

File.foreach("./8.input") do |line|
    if /^[LR]+$/.match? line
        processInstructionLine line, instructions
    end

    continue if line == ""
    
    if /[0-9A-Z]{3} \= \([0-9A-Z]{3}, [0-9A-Z]{3}\)/.match? line
        processMapLine line, map, startingNodes, endingNodes
    end
end

endingNodes = Set.new(endingNodes)
p "#{instructions.size} instructions, #{map.size} nodes (#{startingNodes.size} starting, #{endingNodes.size} ending)"

counts = []
startingNodes.each do |node|
    count = walkTheMap instructions, map, node, endingNodes
    counts << count
    p "#{node}: #{count} steps"
end

p "Steps to all synchronized finish: #{getLcm(counts)}"