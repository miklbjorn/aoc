use std::fmt::Display;

pub mod day01;

pub struct SolutionSet<O1: Display, O2: Display> {
    pub part1: Option<O1>,
    pub part2: Option<O2>,
}

pub fn get_solver(day: i32) -> impl Solver {
    match day {
        1 => day01::Solution,
        _ => panic!("No solver for day {}", day)
    }
}

pub trait Solver {
    type I;
    type O1: Display;
    type O2: Display;

    fn parse_input(&self, input: &str) -> Self::I;
    fn part_1(&self, input: &Self::I) -> Option<Self::O1>;
    fn part_2(&self, input: &Self::I) -> Option<Self::O2>;

    fn solve(&self, input: &str) -> SolutionSet<Self::O1, Self::O2> {

        let input: Self::I = self.parse_input(input);
    
        let sol1: Option<Self::O1> = self.part_1(&input);
        let sol2: Option<Self::O2> = self.part_2(&input);
    
        SolutionSet {
            part1: sol1,
            part2: sol2,
        }
    }


}