Pipes = {
    "|" => :vert,
    "-" => :horz,
    "L" => :ur,
    "J" => :ul,
    "F" => :,
    "7" => :sw,
    "." => :gnd,
    "S" => :start
}

def getNextMove(map, px, py, cx, cy, steps)
    rx = cx - px
    ry = cx - py

end

def testForStart(map, px, py, cx, cy, steps)
    return steps if map[cy][cx] == :start
    getNextMove(map, px, py, cx, cy, steps)
end

# ~

map = []
File.foreach("./10.input") do |line|
    mapline = [:gnd]
    mapline += line.strip.chars.map { |c| Pipes[c] }
    mapline << :gnd
    map << mapline
end
moat = map[0].map { |d| :gnd }
map.unshift(moat)
map.push(moat)

p map