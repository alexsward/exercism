pub fn raindrops(n: u32) -> String {
    let mut result: String = String::new();
    if n % 3 == 0 {
        result.push_str("Pling");
    }
    if n % 5 == 0 {
        result.push_str("Plang");
    }
    if n % 7 == 0 {
        result.push_str("Plong");
    }
    match result.len() {
        0 => n.to_string(),
        _ => result
    }
}
