use std::fs::File;
use std::io::{Result, BufReader, BufRead};

mod mapping;
use mapping::SpaceMap;

fn read_file(path: &str) -> Result<SpaceMap> {
    let mut space_map = SpaceMap::new();
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    for line in reader.lines() {
        space_map.add_row(line?);
    }
    return Ok(space_map);
}

fn main() {
    let space_map: SpaceMap = read_file("/Users/tpsavard/Development/GitHub/tpsavard/Advent-of-Code-2023/Rust/day11/11.input").unwrap();
}
