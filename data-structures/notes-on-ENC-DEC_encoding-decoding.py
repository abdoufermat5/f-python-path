# coding: utf-8
if __name__ == "__main__":
    my_cafe = "Café chaud"
    ENCODING = "ascii"
    print("encode by ignoring errors", my_cafe.encode(encoding=ENCODING, errors="ignore"))
    # output: b'Caf chaud' => you lose the data
    print("encode by replacing errors by '?'", my_cafe.encode(encoding=ENCODING, errors="replace"))
    # output: b'Caf? chaud' => you lose the data but at least you know where it was
    print("encode by replacing errors by xml entity", my_cafe.encode(encoding=ENCODING, errors="xmlcharrefreplace"))
    # output: b'Caf&#233; chaud' => you don't lose the data

    f = open("data/cafe.txt", "w", encoding="utf-8")
    f.write("Café chaud")
    f.close()
    f = open("data/cafe.txt")
    print(f.read())
    f.close()
    fb = open("data/cafe.txt", "rb")
    print(fb.read())
    import os

    print(os.stat("data/cafe.txt"))

    print("\n" * 20)

    import locale
    import sys

    expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """
    my_file = open("data/dummy", "w")

    for expression in expressions.split():
        value = eval(expression)
        print(f"{expression:>30} -> {value!r}")

    print("\n" * 20)

    from unicodedata import normalize, name

    half = "\N{VULGAR FRACTION ONE HALF}"
    print(half)  # output: ½
    nfkc_half = normalize("NFKC", half)
    print(nfkc_half)  # output: 1/2

    for ch in nfkc_half:
        print(ch, name(ch), sep="\t")

    nfkd_half = normalize("NFKD", half)
    print(nfkd_half)
    for ch in nfkd_half:
        print(ch, name(ch), sep="\t")

    # BEWARE
    four_squared = '4²'
    nfkc_four_squared = normalize("NFKC", four_squared) # ouput: 42 which doesn't make sens!
    print(nfkc_four_squared)

