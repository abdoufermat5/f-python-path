# Special Methods for Sequences

> *Don't check whether it is-a duck: check whether it quacks-like-a duck, walks-like-a duck, etc, etc, depending on
exactly what subset of duck-like behaviour you need to play your language-games with.* (comp.lang.python, July 26, 2000)
> -- Alex Martelli

## Vector Space Model

Vector space model or term vector model is an algebraic model for representing text documents (or more generally, items)
as vectors such that the distance between vectors represents the relevance between the documents. It is used in
information filtering, information retrieval, indexing and relevancy rankings. Its first use was in the [SMART
Information Retrieval System](https://en.wikipedia.org/wiki/SMART_Information_Retrieval_System).

## Python reprlib

The `reprlib` module provides a version of `repr()` customized for abbreviated displays of large or deeply nested
containers. This module is especially useful for visualizing very large data structures or data structures with large
numbers of nested containers.

**Example:**

```python
import reprlib

reprlib.repr(set('supercalifragilisticexpialidocious'))
# "{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

## Protocol and Duck Typing

In computer programming, duck typing is an application of the duck test in type safety. It requires that type checking be
deferred to runtime, and is implemented by means of dynamic typing or reflection. Duck typing is concerned with
establishing the suitability of an object for some purpose, using the principle, "If it looks like a duck and quacks like
a duck, it must be a duck."

**Python performs type checking at runtime, and is a dynamically typed language. While typed languages (like C, C++, Java,
etc.) perform type checking at compile time, and are statically typed languages.**

In the context of Object-Oriented Programming, a protocol is an informal interface, defined only in documentation and not
in code. For example, the sequence protocol in Python entails just the `__len__` and `__getitem__` methods. Any class
that provides these methods can be used wherever a sequence is expected.

Implementing the `__len__` and `__getitem__` methods in a class makes it a sequence, and that means we can use indexing
and slicing on the class objects.

**Example:**

```python
class Foo:
    def __len__(self):
        return 42

    def __getitem__(self, pos):
        return pos

f = Foo()
print(len(f))  # 42
print(f[2])  # 2
print(f[3:5])  # slice(3, 5, None)
```

### Python __getattr__ 

The `__getattr__` method is called when the requested attribute is not found in the usual places (i.e., it is not an
instance attribute nor is it found in the class tree for the instance). This method is called only when the attribute
access fails.

**Example:**

```python
class Foo:
    def __init__(self):
        baz = 'foo'
    def __getattr__(self, name):
        return name

f = Foo()
print(f.bar)  # bar
print(f.baz)  # foo
```
```

Here's a weird scenario:

```python
>>> v = VectorND(range(10))
>>> v.x
0
>>> v.x = 45
>>> v.x
45
>>> v
VectorND([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

The `v.x` attribute is not found in the class tree, so `__getattr__` is called, and it returns the attribute name. But when
we assign a value to `v.x`, it creates an instance attribute `x` and the `__getattr__` method is not called.
So to avoid this kind of confusion, we can use the `__setattr__` method to prevent the creation of new instance
attributes that belong to the class `__match_args__` list (in this case, ['x', 'y', 'z', 't']).


## Hashing a multidimensional vector

We can use the `functools.reduce` function to hash a multidimensional vector. The `functools.reduce` function applies a
function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a
single value.

## Python zip function

The `zip` function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument
sequences or iterables. The iterator stops when the shortest input iterable is exhausted.

The `zip` function can be used to transpose a matrix. The `*` operator can be used to unpack the zipped tuples.

**Example:**

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))

# Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

## Python itertools.chain function

The `itertools.chain` function returns an iterator that produces elements from the first iterable until it is exhausted,
then it continues to the next iterable, until all of the iterables are exhausted.

**Example:**

```python
from itertools import chain

radius = 10
angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
spherical_coordinates = chain([radius], angles)

# Output: [10, 0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
```

## The KISS Principle

The KISS principle states that most systems work best if they are kept simple rather than made complicated; therefore,
simplicity should be a key goal in design, and unnecessary complexity should be avoided.

KISS is an acronym for "Keep it simple, stupid" as a design principle noted by the U.S. Navy in 1960.
