
#[derive(Debug, Clone)]
pub struct IntcodeProgram {
    pub memory: Vec<i32>,
}


impl IntcodeProgram {
    pub fn new(memory: Vec<i32>) -> IntcodeProgram {
        IntcodeProgram {
            memory,
        }
    }

    pub fn from_string(input: &str) -> IntcodeProgram {
        let memory: Vec<i32> = input
            .trim()
            .split(',')
            .map(|s| s.parse().expect("Could not parse int"))
            .collect();
        print!("{:?}", memory);
        IntcodeProgram::new(memory)
        
    }
}

#[derive(Debug)]
pub struct IntcodeComputer {
    pub memory: Vec<i32>,
    pub instruction_pointer: usize,
}

impl IntcodeComputer {

    pub fn new(program: IntcodeProgram) -> IntcodeComputer {
        IntcodeComputer {
            memory: program.memory.clone(),
            instruction_pointer: 0,
        }
    }

    pub fn run(&mut self) -> i32 {
        const HALT: i32 = 99;

        'program: loop {
            let opcode = self.memory[self.instruction_pointer];
            match opcode {
                1 => self.op_01_add(),
                2 => self.op_02_mul(),
                HALT => break 'program,
                _ => panic!("Unknown opcode: {}", opcode),
                
            }
        }
        self.memory[0]
    }

    fn op_01_add(&mut self) {
        let memory = &mut self.memory;
        let instruction_pointer = &self.instruction_pointer;
        let a = memory[memory[instruction_pointer + 1] as usize];
        let b = memory[memory[instruction_pointer + 2] as usize];
        let dest = memory[instruction_pointer + 3] as usize;
        memory[dest] = a + b;
        self.instruction_pointer += 4;
    }

    fn op_02_mul(&mut self) {
        let memory = &mut self.memory;
        let instruction_pointer = &self.instruction_pointer;
        let a = memory[memory[instruction_pointer + 1] as usize];
        let b = memory[memory[instruction_pointer + 2] as usize];
        let dest = memory[instruction_pointer + 3] as usize;
        memory[dest] = a * b;
        self.instruction_pointer += 4;
    }
        

    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_computer_1_test_add() {
        let input = IntcodeProgram::from_string("1,1,1,4,99,5,6,0,99\n");
        let mut computer = IntcodeComputer::new(input);
        assert_eq!(computer.run(), 30);
    }

    #[test]
    fn test_computer_2_test_mult() {
        let input = IntcodeProgram::from_string("2,1,1,4,99,5,6,0,99\n");
        let mut computer = IntcodeComputer::new(input);
        assert_eq!(computer.run(), 11);
    }

}