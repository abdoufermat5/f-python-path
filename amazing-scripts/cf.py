import sys
import unicodedata

START, END = ord(" "), sys.maxunicode + 1


def find(*qw, start=START, end=END):
    q = {w.upper() for w in qw}
    for code in range(start, end):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name and q.issubset(name.split()):
            print(f"U+{code:04X}\t{name}")


def main(words):
    if words:
        find(*words)
    else:
        print("Please provide words to find.")


if __name__ == "__main__":
    main(sys.argv[1:])