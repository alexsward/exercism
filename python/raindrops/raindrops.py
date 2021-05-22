def convert(number: int) -> str:
    output: str = ""
    if number % 3 == 0:
        output += "Pling"
    if number % 5 == 0:
        output += "Plang"
    if number % 7 == 0:
        output += "Plong"
    return str(number) if not output else output
