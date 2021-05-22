import re
from typing import Dict


def count_words(sentence: str) -> Dict[str, int]:
    regex = re.compile("[a-z0-9]+(['][a-z]+)?")

    counts: Dict[str, int] = dict()
    for word in regex.finditer(sentence.lower()):
        word: str = word.group(0)
        if word not in counts:
            counts[word] = 0
        counts[word] = counts[word] + 1
    return counts
