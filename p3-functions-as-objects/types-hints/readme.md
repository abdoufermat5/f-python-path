# Quick Notes

*There are many definitions of the concept of type in the literature. Here
we assume that type is a set of values and a set of functions that one can
apply to these values.*
**--PEP 483: The Theory of Type Hints**

### Python ignore types at runtime

```python
from collections import abc


def double(x: abc.Sequence) -> abc.Sequence:
    return x * 2
```

A type checker will reject that code!!
If you tell Mypy that x is of type `abc.Sequence`, it will flag x*2 as an error because the Sequence ABC does not
implement the `__mul__` method. At runtime, however, Python will happily execute that code, because Python ignores
type annotations by default. But the type checker only cares about what is explicitly declared, and abc.Sequence has no
`__mul__`.

### Duck typing vs Nominal typing

Duck typing and nominal typing are two different approaches to type checking in programming languages.

**Duck typing** is a style of typing in which an object is considered to be of a type if it has the methods and
properties required for that type. This means that the type of an object is determined at runtime, based on its actual
behavior, rather than being explicitly declared at compile time.

**Nominal typing**, on the other hand, is a style of typing in which an object is considered to be of a type if it is
declared as such. This means that the type of an object is static, and does not change at runtime.

Python is a dynamically typed language, which means that it uses duck typing. This makes Python a very flexible
language, as it allows objects of different types to be used interchangeably. However, duck typing can also make Python
programs more difficult to debug, as type errors may not be caught until runtime.

Here is an example of duck typing in Python:

```python
def quack(object):
    if hasattr(object, 'quack'):
        object.quack()
    else:
        raise Exception('Object does not have a quack method')
```

This function takes any object as input and calls its `quack` method if it has one. If the object does not have
a `quack` method, a runtime error is raised.

Here is an example of nominal typing in Python:

```python
class Duck:
    def quack(self):
        print('Quack!')


def quack(duck):
    duck.quack()
```

This code defines a `Duck` class and a `quack` function. The `quack` function takes an object of type `Duck` as input.
This is because the `quack` function is defined inside the `Duck` class, so it can only be called on objects of that
type.

In general, duck typing is more common in Python than nominal typing. This is because duck typing allows for more
flexibility and code reusability. However, nominal typing can be useful for ensuring type safety, especially in large or
complex programs.

Here is a table that summarizes the key differences between duck typing and nominal typing:

| Feature          | Duck typing                | Nominal typing                     |
|------------------|----------------------------|------------------------------------|
| Type checking    | Dynamic at runtime         | Static at compile time             |
| Type inference   | Based on object's behavior | Based on object's type declaration |
| Code flexibility | More flexible              | Less flexible                      |
| Type safety      | Less type safe             | More type safe                     |


### The `Any` type

The `Any` type is a special type that can be used to indicate that a variable can be of any type. This is useful when
you want to write code that is generic and can be used with different types of data.

### Gradual typing

Gradual typing is a type system that allows for both static and dynamic typing. It is a compromise between static typing
and dynamic typing, and is intended to combine the benefits of both approaches.

In a gradual type system, there is a relationship called `consistent-with`, which apply wherever `subtype-of` (most traditional
Object-Oriented nominal type systems rely on) applies, with special rules for type `Any`.

The rules for `consistent-with` are:

1. Given `T1` and a subtype `T2`, then `T2` is consistent with `T1` (Liskov substitution principle).
2. Every type is consistent with `Any`: you can pass objects of every type to an argument declared as `Any`.
3. `Any` is consistent with every type: you can pass an object of type `Any` where an argument of another type is
   expected.

**Example illustrating rules 2 and 3:**

```python
from typing import Any

class T1:
    pass

class T2(T1):
    pass

# rule 2:
def f(x: Any) -> None:
    return x

o0 = object()
o1 = T1()
o2 = T2()

f(o0) # OK
f(o1) # OK
f(o2) # OK

# rule 3:
def g():
    pass

o4 = g()  # inferred type is Any

f1(o4) # OK
f2(o4) # OK
f3(o4) # OK
```


