use super::Solver;

pub struct Solution;

impl Solver for Solution {
    type I = Vec<i32>;
    type O1 = String;
    type O2 = String;

    fn parse_input(&self, input: &str) -> Vec<i32>{
        input
            .lines()
            .map(|line| line.parse().expect("The input rows should all be numbers"))
            .collect()
    }
    
    fn part_1(&self, input: &Vec<i32>) -> Option<String> {
        input
            .iter()
            .map(|mass| mass / 3 - 2)
            .sum::<i32>()
            .to_string()
            .into()
    }
    
    fn part_2(&self, input: &Vec<i32>) -> Option<String> {
        input
            .iter()
            .map(|mass| {
                let mut total = 0;
                let mut fuel = mass / 3 - 2;
                while fuel > 0 {
                    total += fuel;
                    fuel = fuel / 3 - 2;
                }
                total
            })
            .sum::<i32>()
            .to_string()
            .into()
    }

}





#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_INPUT: &str = "12\n";

    // #[test]
    // fn test_part_1() {
    //     let input = parse_input(EXAMPLE_INPUT);
    //     assert_eq!(part_1(&input), Some("2".to_string()));
    // }
}