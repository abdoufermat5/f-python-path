import sys
import re
import unicodedata
from typing import Iterator, Dict, Union, Set

RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1


def tokenize(text: str) -> Iterator[str]:
    for match in RE_WORD.finditer(text):
        yield match.group()


def name_index(start: int = 32, end: int = STOP_CODE) -> Dict[str, Set[str]]:
    index: Dict[str, Set[str]] = {}
    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ""):
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)
    return index


if __name__ == '__main__':
    
    text = 'Hi, I am a text!'

    token = name_index(32, 97)
    for key in token:
        print(key, token[key])
