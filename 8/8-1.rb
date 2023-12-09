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

def processMapLine(line, map)
    md = /([A-Z]{3}) \= \(([A-Z]{3}), ([A-Z]{3})\)/.match line
    map[md.captures[0]] = { left: md.captures[1], right: md.captures[2] }
end

def walkTheMap(instructions, map)
    steps = 0
    cur = "AAA"
    while cur != "ZZZ"
        options = map[cur]
        cur = options[instructions[steps % instructions.size]]
        steps += 1
    end
    return steps
end

# ~

instructions = []
map = {}

File.foreach("./8.input") do |line|
    if /^[LR]+$/.match? line
        processInstructionLine line, instructions
    end

    continue if line == ""
    
    if /[A-Z]{3} \= \([A-Z]{3}, [A-Z]{3}\)/.match? line
        processMapLine line, map
    end
end

p "#{instructions.size} instructions, #{map.size} nodes"
p "#{walkTheMap instructions, map} steps"