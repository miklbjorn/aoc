
// TODO 
// [ ] add argument parsing
// [x] download and parse input if needed
// [x] pattern for test input -> using unit tests
// [x] make a main runner function
// [ ] make a template for new days and code to to execute them
// [ ] refactor to allow for multiple years


mod solutions;
mod input;
mod intcode;


fn main() {

    let day = 2;    
    
    let input = input::get_input(day);
    let solver = solutions::get_solver(day);
    
    let solutions = solver(&input);

    println!("{}", solutions.part1.unwrap_or("No solution to part 1.".to_string()));
    println!("{}", solutions.part2.unwrap_or("No solution to part 2.".to_string()));

   
}



