from vector2D import Vector2D, ShortVector2D
from random import randint


def keyword_pattern(v: Vector2D):
    match v:
        case Vector2D(x=0, y=0):
            print(f"{v!r} is null vector")
        case Vector2D(x=0):
            print(f"{v!r} is vertical vector")
        case Vector2D(_, y=0):  # this works because of the __match_args__ = ("x", "y") in the class
            print(f"{v!r} is horizontal vector")
        case Vector2D(x=x, y=y) if x == y:
            print(f"{v!r} is diagonal vector")
        case _:
            print(f"{v!r} is a generic vector")


if __name__ == "__main__":
    v1 = Vector2D(3, 4)
    print(v1.__dict__)
    print(v1.x, v1.y)
    x, y = v1
    print(x, y)

    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    print(v1)
    print(v1_clone)
    print(bytes(v1))
    print(abs(v1))
    print(bool(v1), bool(Vector2D(0, 0)))
    print(format(v1, ".2e"))
    print(format(v1, ".2fp"))

    v2 = Vector2D.frombytes(bytes(v1))
    print(v2)
    print("inside the from bytes")
    bytes_ = b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
    t = chr(bytes_[0])  # typecode is 'd' for double
    print(t)
    memv = memoryview(bytes_[1:]).cast(t)  # this will be a memoryview of typecode 'd'
    print(*memv)  # this will be the unpacked array of doubles

    set_vectors = set(Vector2D(randint(0, 10), randint(0, 10)) for i in range(10))
    print(set_vectors)
    print(len(set_vectors))

    print(f"{v1!r}")

    print(complex(v1))

    z = 3 + 9j
    v_z = Vector2D.fromcomplex(z)

    print(v_z)
    print(complex(v_z))
    print(complex(v_z) == z)

    keyword_pattern(Vector2D(0, 0))
    keyword_pattern(Vector2D(0, 5))
    keyword_pattern(Vector2D(5, 0))
    keyword_pattern(Vector2D(5, 5))
    keyword_pattern(Vector2D(3, 4))

    print("--------------------------------")
    print("compare bytes length of Vector2D and ShortVector2D")
    print("--------------------------------")
    v1 = Vector2D(3, 4)
    v2 = ShortVector2D(3, 4)
    print(len(bytes(v1)))  # 17
    print(len(bytes(v2)))  # 9
