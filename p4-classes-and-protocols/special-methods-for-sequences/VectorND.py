import itertools
import operator
from array import array
import reprlib
import math
import functools


class VectorND:
    """
    A class to represent a vector in n-dimensional space.

    A `VectorND` is built from an iterable of numbers. The number of dimensions is determined by the length of the
    iterable. The components of the vector are stored in an array of `d` (double precision float) type.

        >>> VectorND([3.1, 4.2])
        VectorND([3.1, 4.2])
        >>> VectorND([3, 4, 5])
        VectorND([3.0, 4.0, 5.0])
        >>> VectorND(range(10))
        VectorND([0.0, 1.0, 2.0, 3.0, 4.0, ...]) # repr() shows at most 30 characters

    Tests with two-dimensional vectors:

        >>> v2 = VectorND([3, 4])
        >>> x, y = v2
        >>> x, y
        (3.0, 4.0)
        >>> v2
        VectorND([3.0, 4.0])
        >>> v2_clone = eval(repr(v2))
        >>> v2 == v2_clone
        True
        >>> print(v2)
        (3.0, 4.0)
        >>> octets = bytes(v2)
        >>> octets
        b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
        >>> abs(v2)
        5.0
        >>> bool(v2)
        True
        >>> bool(VectorND([0, 0]))
        False

    Test of the `frombytes` class method:

        >>> v1 = VectorND([3, 4])
        >>> v1_clone = VectorND.frombytes(bytes(v1))
        >>> v1 == v1_clone
        True

    Tests with three-dimensional vectors:

        >>> v3 = VectorND([3, 4, 5])
        >>> x, y, z = v3
        >>> x, y, z
        (3.0, 4.0, 5.0)
        >>> v3
        VectorND([3.0, 4.0, 5.0])
        >>> v3_clone = eval(repr(v3))
        >>> v3 == v3_clone
        True
        >>> print(v3)
        (3.0, 4.0, 5.0)
        >>> abs(v3) # doctest: +ELLIPSIS
        7.071067811...
        >>> bool(v3)
        True
        >>> bool(VectorND([0, 0, 0]))
        False

    Tests with many-dimensional vectors:

        >>> v10 = VectorND(range(10))
        >>> v10
        VectorND([0.0, 1.0, 2.0, 3.0, 4.0, ...]) # repr() shows at most 30 characters
        >>> v10.x, v10.y, v10.z
        (0.0, 1.0, 2.0)
        >>> v10.t
        3.0
        >>> abs(v10) # doctest: +ELLIPSIS
        16.881943016...

    Tests with `__bytes__` and `frombytes` methods:

        >>> v10 = VectorND(range(10))
        >>> v10_clone = VectorND.frombytes(bytes(v10))
        >>>v10_clone
        VectorND([0.0, 1.0, 2.0, 3.0, 4.0, ...]) # repr() shows at most 30 characters
        >>> v10 == v10_clone
        True

    Tests of sequence and slicing behavior:

        >>> v10 = VectorND(range(10))
        >>> v10[0:3]
        VectorND([0.0, 1.0, 2.0])
        >>> v10[1:4][0]
        1.0
        >>> v10[-1]
        9.0
        >>> v10[1:4][1:2]
        VectorND([2.0])
        >>> len(v10)
        10

    Dynamic attribute lookup failure:

        >>> v10 = VectorND(range(10))
        >>> v10.k
        Traceback (most recent call last):
        ...
        AttributeError: 'VectorND' object has no attribute 'k'
        >>> v3 = VectorND([3, 4, 5])
        >>> v3.t
        Traceback (most recent call last):
        ...
        AttributeError: 'VectorND' object has no attribute 't'
        >>> v3.spam
        Traceback (most recent call last):
        ...
        AttributeError: 'VectorND' object has no attribute 'spam'

    Tests of hashing:

        >>> v1 = VectorND([3, 4])
        >>> v2 = VectorND([3.1, 4.2])
        >>> hash(v1) == hash(v2)
        False
        >>> v3 = VectorND([3, 4, 5])
        >>> hash(v3)
        7
        >>> v4 = VectorND([3, 4, 5, 6])
        >>> hash(v4)
        2

    Most hash codes of non-integers vary from a 32-bit to a 64-bit CPython build.

        >>> import sys
        >>> v5 = VectorND([3, 4, 5, 6, 7])
        >>> hash(v5) == (384307168202284039 if sys.maxsize > 2**32 else 357915986)
        True

    Test of the `__format__` method:

        >>> v2 = VectorND([3, 4])
        >>> format(v2)
        '(3.0, 4.0)'
        >>> format(v2, '.2f')
        '(3.00, 4.00)'
        >>> format(v2, '.3e')
        '(3.000e+00, 4.000e+00)'
        >>> format(v2, 'h')
        '<5.0, 0.9272952180016122>'
        >>> v3 = VectorND([3, 4, 5])
        >>> format(v3, 'h') # doctest: +ELLIPSIS
        '<7.0710678118654755, 0.9272952180016122, 0.8960553845713439>'
        >>> format(v3, '.3e')
        '(3.000e+00, 4.000e+00, 5.000e+00)'
        >>> format(v3, '.3fh')
        '<7.071, 0.927, 0.896>'
        >>> v4 = VectorND([3, 4, 5, 6])
        >>> format(v4, '.3fh')
        '<9.273, 0.896, 0.876, 0.860>'
    """
    typecode = "d"
    __match_args__ = ("x", "y", "z", "t")

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("["):-1]
        return f"VectorND({components})"

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        if isinstance(index, slice):
            cls = type(self)
            return cls(self._components[index])
        index = operator.index(index)
        return self._components[index]

    def __getattr__(self, name):
        cls = type(self)

        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f"{cls.__name__!r} object has no attribute {name!r}"
        raise AttributeError(msg)

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.__match_args__:
                error = "readonly attribute {attr_name!r}"
            elif name.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ""
            if error:
                msg = error.format(attr_name=name, cls_name=cls.__name__)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)

        return cls(memv)

    def angle(self, n):
        r = math.hypot(self[n:])  # distance from origin to projection on xy plane
        a = math.atan2(r, self[n - 1])  # 0 <= a <= π
        if n == len(self) - 1 and self[-1] < 0:  # last spherical coordinate is azimuthal angle
            return math.pi * 2 - a  # 0 <= θ <= 2π
        else:
            return a  # 0 <= a <= π other than azimuthal angle

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))  # start from 1 to skip radial coordinate

    def __format__(self, fmt_spec=""):
        if fmt_spec.endswith("h"):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())  # produces something like (r, θ, φ) for 3D
            outer_fmt = "<{}>"
        else:
            coords = self
            outer_fmt = "({})"
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(", ".join(components))
