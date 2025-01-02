use super::SolutionSet;

fn parse_input(input: &str) -> Vec<i32>{
    input
        .lines()
        .map(|line| line.parse().expect("The input rows should all be numbers"))
        .collect()
}

fn part_1(input: &Vec<i32>) -> Option<String> {
    input
        .iter()
        .map(|mass| mass / 3 - 2)
        .sum::<i32>()
        .to_string()
        .into()
}

fn part_2(input: &Vec<i32>) -> Option<String> {
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

pub fn solve(input: &str) -> SolutionSet {
    let input = parse_input(input);

    let part1 = part_1(&input);
    let part2 = part_2(&input);

    SolutionSet {
        part1,
        part2,
    }
}
