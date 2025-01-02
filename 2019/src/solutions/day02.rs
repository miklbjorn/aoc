use crate::intcode::{IntcodeProgram, IntcodeComputer};

use super::SolutionSet;

fn parse_input(input: &str) -> IntcodeProgram{
    IntcodeProgram::from_string(input)
}

fn part_1(input: &IntcodeProgram) -> Option<String> {
    let mut program = input.clone();
    program.memory[1] = 12;
    program.memory[2] = 2;

    let mut computer = IntcodeComputer::new(program);
    let result = computer.run();
    Option::from(result.to_string())
}

fn part_2(input: &IntcodeProgram) -> Option<String> {
    
    for i in 0..=99 {
        for j in 0..=99 {
            let mut program = input.clone();
            program.memory[1] = i;
            program.memory[2] = j;

            let mut computer = IntcodeComputer::new(program);
            let result = computer.run();
            if result == 19690720 {
                return Some((100 * i + j).to_string());
            }
        }
    };
    None
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







