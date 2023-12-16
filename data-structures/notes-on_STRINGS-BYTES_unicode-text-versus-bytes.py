if __name__ == "__main__":
    str1 = "café"
    bytes1 = str1.encode("utf-8")
    print("encoded string", bytes1)
    # same as
    bytes2 = bytes(str1, encoding="utf-8")
    print("encoded string", bytes2)
    print("\n" * 10)

    # indexing

    print("bytes1[0]", bytes1[0])  # output 99 because each item is an integer from 0 to 255
    print("bytes1[1]", bytes1[1])  # output 97 //
    print("bytes1[2]", bytes1[:1])  # output b'c' because Slices of bytes are also bytes—even slices of a single byte.
    print("\n" * 10)
    # arrays
    import array

    numbers = array.array("h", [0, 1, 2])
    print("numbers", numbers)
    octets = bytes(numbers)
    print("octets", octets)  # output: octets b'\x00\x00\x01\x00\x02\x00'
    numbers2 = array.array("I", [0, 1, 2])
    print("numbers2 ", numbers2)
    octets2 = bytes(numbers2)
    print("octets2", octets2)  # output: octets2 b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00'
    print("\n"*10)
    # errors
    cafe = "café"
    # we can encode this using encoding that does not support é character, for example ascii
    ENCODING = "iso8859_1"
    try:
        bytes_ = cafe.encode(encoding=ENCODING)
        print("encoded in ", ENCODING, " result: ", bytes_)
    except UnicodeEncodeError as e:
        print("Invalid encoding", ENCODING)
        raise e
