
// TODO 
// [ ] add argument parsing
// [x] download and parse input if needed
// [x] pattern for test input -> using unit tests
// [x] make a main runner function
// [ ] make a template for new days and code to to execute them
// [ ] refactor to allow for multiple years

use solutions::Solver;

mod solutions;
mod input;


fn main() {

    let day = 1;    
    
    let input = input::get_input(day);
    let solver = solutions::get_solver(day);
    
    let solutions = solver.solve(&input);

    println!("{}", solutions.part1.unwrap());
    println!("{}", solutions.part2.unwrap());
}



