from typing import Optional


def two_fer(name: Optional[str] = None) -> str:
    if not name:
        return "One for you, one for me."
    return f"One for {name}, one for me."
