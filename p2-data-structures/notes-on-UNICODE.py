import pyuca
import unicodedata

if __name__ == '__main__':
    coll = pyuca.Collator()

    words = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
    # a normal sort would give this: ['acerola', 'atemoia', 'açaí', 'caju', 'cajá']
    # but with pyuca, we get this:
    print(sorted(words, key=coll.sort_key))
    # ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']

    # list of emoji
    emojis = ["😅", "👏", "🥳", "🎉"]
    for emoji in emojis:
        print(f"Name of {emoji} is ", unicodedata.name(emoji), " code point is: ", ord(emoji))

    # Output:
    # Name of 😅 is  SMILING FACE WITH OPEN MOUTH AND COLD SWEAT
    # Name of 👏 is  CLAPPING HANDS SIGN
    # Name of 🥳 is  FACE WITH PARTY HORN AND PARTY HAT
    # Name of 🎉 is  PARTY POPPER
