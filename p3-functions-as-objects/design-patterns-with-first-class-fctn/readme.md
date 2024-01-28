# Design Patterns with First-Class Functions

> "Conformity to patterns is not a measure of goodness." - Ralph Johnson

[RECALL]

In programming, a **first-class function** is a concept that treats functions as first-class citizens. This means that
functions are treated like any other variable. Specifically, a language with first-class functions allows functions to
be:

1. **Assigned to variables:** Functions can be stored in variables, data structures, or passed as arguments to other
   functions.

2. **Passed as arguments to other functions:** Functions can be used as arguments to other functions, just like
   integers, strings, or other types.

3. **Returned from other functions:** Functions can be created inside other functions and returned as an output, just
   like any other data type.

4. **Stored in data structures:** Functions can be stored in arrays, lists, dictionaries, or other data structures.

Languages that support first-class functions often support higher-order functions, which are functions that take other
functions as arguments or return them as results. JavaScript, Python, and Ruby are examples of languages that treat
functions as first-class citizens. This capability is central to many programming techniques and paradigms, such as
functional programming, where functions are used to express logic in a succinct and expressive manner.


## Strategy Pattern

The **strategy pattern** is a behavioral design pattern that enables selecting an algorithm at runtime. Instead of
implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to
use.

## Command Pattern

The **command pattern** is a behavioral design pattern that turns a request into a stand-alone object that contains all
information about the request. This transformation lets you parameterize methods with different requests, delay or
queue a request’s execution, and support undoable operations.

---

## The __call__ of the Wild

If functions have a `__call__` method, and methods are callable, do `__call__` methods also have `__call__` methods?

Here's **Leonardo Rochael**'s discovery:

```python

def turtle():
    return "eggs"

print(turtle.__call__())
# outputs: eggs

print(turtle.__call__.__call__())
# outputs: eggs

print(turtle.__call__.__call__.__call__())
# outputs: eggs

print(turtle.__call__.__call__.__call__.__call__())
# outputs: eggs

print(turtle.__call__.__call__.__call__.__call__.__call__())
# outputs: eggs

print(turtle.__call__.__call__.__call__.__call__.__call__.__call__())
# outputs: eggs

```

**Turtles all the way down!**