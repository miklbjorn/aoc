
pub mod day01;
pub mod day02;

pub struct SolutionSet {
    pub part1: Option<String>,
    pub part2: Option<String>,
}

pub fn get_solver(day: i32) -> fn(&str) -> SolutionSet{
    match day {
        1 => day01::solve,
        2 => day02::solve,
        _ => panic!("No solver for day {}", day)
    }
}



