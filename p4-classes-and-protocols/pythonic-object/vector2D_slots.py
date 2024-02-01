from array import array
import math


class Vector2D:
    """
    A two-dimensional vector class

        >>> v1 = Vector2D(3, 4)
        >>> print(v1.x, v1.y)
        3.0 4.0
        >>> x, y = v1
        >>> x, y
        (3.0, 4.0)
        >>> v1
        Vector2D(3.0, 4.0)
        >>> v1_clone = eval(repr(v1))
        >>> v1 == v1_clone
        True
        >>> print(v1)
        (3.0, 4.0)
        >>> octets = bytes(v1)
        >>> octets
    b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
        >>> abs(v1)
        5.0
        >>> bool(v1), bool(Vector2D(0, 0))
        (True, False)

    Test of ``.frombytes()`` class method:

        >>> v1_clone = Vector2D.frombytes(bytes(v1))
        >>> v1_clone
        Vector2D(3.0, 4.0)
        >>> v1 == v1_clone
        True

    Tests of ``format()`` with Cartesian coordinates:

        >>> format(v1)
        '(3.0, 4.0)'
        >>> format(v1, '.2f')
        '(3.00, 4.00)'
        >>> format(v1, '.3e')
        '(3.000e+00, 4.000e+00)'

    Tests of the ``angle`` method:

        >>> Vector2D(0, 0).angle()
        0.0
        >>> Vector2D(1, 0).angle()
        0.0
        >>> epsilon = 10**-8
        >>> abs(Vector2D(0, 1).angle() - math.pi/2) < epsilon
        True
        >>> abs(Vector2D(1, 1).angle() - math.pi/4) < epsilon
        True

    Tests of ``format()`` with polar coordinates:

        >>> format(Vector2D(1, 1), 'p')  # doctest:+ELLIPSIS
        '<1.414213..., 0.785398...>'
        >>> format(Vector2D(1, 1), '.3ep')
        '<1.414e+00, 7.854e-01>'
        >>> format(Vector2D(1, 1), '0.5fp')
        '<1.41421, 0.78540>'

    Tests of `x` and `y` read-only properties:

        >>> v1.x, v1.y
        (3.0, 4.0)
        >>> v1.x = 123
    Traceback (most recent call last):
        ...
    AttributeError: can't set attribute `x`

    Tests of hashing:

        >>> v1 = Vector2D(3, 4)
        >>> v2 = Vector2D(3.1, 4.2)
        >>> hash(v1), hash(v2)
        (7, 384307168202284039)
        >>> len({v1, v2})
        2

    Tests of ``fromcomplex()`` class method:

        >>> z = 3 + 9j
        >>> v_z = Vector2D.fromcomplex(z)
        >>> v_z
        Vector2D(3.0, 9.0)
        >>> complex(v_z) == z
        True
    """

    typecode = "d"
    __match_args__ = ("x", "y")  # this is for pattern matching
    __slots__ = ("__x", "__y")
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):  # this makes x read-only property
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        class_name = type(self).__name__

        return f"{class_name}({self.x!r}, {self.y!r})"

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __format__(self, format_spec=""):
        if format_spec.endswith("p"):  # polar coordinates
            format_spec = format_spec[:-1]
            coords = abs(self), self.angle()
            outer_format = "<{}, {}>"
        else:
            coords = self
            outer_format = "({}, {})"
        components = (format(c, format_spec) for c in coords)  # format each component of a vector
        return outer_format.format(*components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __complex__(self):
        return complex(self.x, self.y)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)  # XOR-ing hash of x and y

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    @classmethod
    def fromcomplex(cls, z: complex):
        return cls(z.real, z.imag)

    def angle(self):
        return math.atan2(self.y, self.x)
