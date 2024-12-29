use std::path::Path;
use std::fs;
use std::env;
use std::io;

const INPUT_DIR: &str = "input";

pub fn get_input(day: i32) -> String {
    let input_file_name = construct_input_file_name(day);

    if !Path::new(&input_file_name).exists() {
        download_input_file(day);
    }

    let input = fs::read_to_string(&input_file_name).expect("Could not read input file: {input_file_name}");
    input
}

fn download_input_file(day: i32) {
    let url = format!("https://adventofcode.com/2019/day/{}/input", day).to_string();
    let cookie = env::var("AOC_SESSION_ID").expect("AOC_SESSION_ID not set");

    let client = reqwest::blocking::Client::new();
    let res = client.get(&url)
        .header("cookie", format!("session={}", cookie))
        .send()
        .expect("Could not download input");

    ensure_input_dir_exists();
    let input_file_name = construct_input_file_name(day);
    let mut file = fs::File::create(&input_file_name).expect("Could not create file");
    println!("{}", format!("Writing input file: {}", input_file_name));
    io::copy(&mut res.bytes().unwrap().as_ref(), &mut file).expect("Could not write to file");
}

fn ensure_input_dir_exists() {
    if !Path::new(INPUT_DIR).exists() {
        println!("{}", format!("Creating input directory: {}", INPUT_DIR));
        fs::create_dir(INPUT_DIR).expect("Could not create input directory");
    }
}

fn construct_input_file_name(day: i32) -> String {
    format!("{}/{}", INPUT_DIR, format!("day{:02}.txt", day))
}