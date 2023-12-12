pub enum Space {
    Empty,
    Galaxy,
}

pub struct SpaceMap {
    rows: Vec<Vec<Space>>
}

impl SpaceMap {
    pub fn new() -> Self {
        Self { rows: Vec::new() }
    }
    
    pub fn add_row(&mut self, line: String) -> () {
        let mut row: Vec<Space> = Vec::new();
        for char in line.chars() {
            match char {
                '.' => { row.push(Space::Empty); () },
                '#' => { row.push(Space::Galaxy); () },
                _ => (),
            };
        }
        self.rows.push(row);
    }
}