from typing import List


def translate(text: str) -> str:
    translated: List[str] = []
    for word in text.split():
        if word[0] in ["a", "e", "i", "o", "u"]:
            translated.append(f"{word}ay")
        else:
            translated.append(f"{word[1:]}{word[0]}ay")
    return " ".join(translated)
