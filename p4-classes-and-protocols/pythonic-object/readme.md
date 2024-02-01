# Chapter 11: Pythonic Object

> "For a library or framework to be Pythonic is to make it as easy and natural as possible for a Python programmer
> to pick up how to perform a task"  -- Martijn Faassen, creator of Python and Javascript frameworks

## Object Representation

Python has two built-in functions that are used to return a string representation of an object.

- `repr()` Return a string representing the object as the developer wants to see it. It’s what you get when the Python
  console or a debugger shows an object.
- `str()` Return a string representing the object as the user wants to see it. It’s what gets printed when you `print()`
  an object.

In Python, the **!r** placeholder in string formatting instructs the formatting engine to use the **repr()** function to
represent the object. This means that the object will be converted to a string that includes backslashes and quotation
marks for any special characters. This is useful for debugging and printing objects that contain special characters.

For example, the following code will print the string representation of the object `"Hello, world!"`:

```python
print("The string is: {!r}".format("Hello, world!"))
```

This will print the following output:

```
The string is: 'Hello, world!'
```

while

```python
print("The string is: {!s}".format("Hello, world!"))
```

will print the following output:

```
The string is: Hello, world!
```

The **!r** placeholder is not as commonly used as the **!s** placeholder, which instructs the formatting engine to use
the **str()** function to represent the object. The **str()** function is more commonly used because it produces more
human-readable strings. However, the **!r** placeholder can be useful for debugging and for printing objects that
contain special characters.

Here is a table that summarizes the differences between the **!r** and **!s** placeholders:

| Placeholder | Formatting Function | Result                                                                                                |
|-------------|---------------------|-------------------------------------------------------------------------------------------------------|
| **!r**      | **repr()**          | String representation of the object, including backslashes and quotation marks for special characters |
| **!s**      | **str()**           | Human-readable string representation of the object                                                    |

### Instance methods, class methods, static methods

Instance methods are the most common type of methods in Python classes. They are used to define behaviors that should be
specific to a particular instance of a class. In other words, we expect that the behavior of an instance method will be
different from one instance to another.

```python
class MyClass:
    def instance_method(self):
        return 'instance method called', self
```

Class methods are methods that are not bound to an object, but to a class. They have the access to the state of the
class as it takes a class parameter that points to the class and not the object instance. It can modify a class state
that would apply across all the instances of the class. For example, it can modify a class variable that will be
applicable to all the instances.

```python
class MyClass:
    def class_method(cls):
        return 'class method called', cls
```

or using the `@classmethod` decorator:

```python
class MyClass:
    @classmethod
    def class_method(cls):
        return 'class method called', cls
```

The `@classmethod` decorator is a built-in decorator that defines a class method. Its most common use is for alternative
constructors.

**When to use class methods?**

- When you need to access or modify the class state.
- When you want to implement factory methods that return an instance of the class, but the instance might be an instance
  of a derived class.
- When the method operates on class data rather than instance data.

Static methods are methods that are bound to a class rather than its object. They do not require a class instance
creation. So, they are not dependent on the state of the object. The difference between a static method and a class
method is: a static method doesn't receive any additional arguments (e.g. `cls` or `self`).

```python
class MyClass:
    def static_method(age):
        return 'static method called'
```

or using the `@staticmethod` decorator:

```python
class MyClass:
    @staticmethod
    def static_method(age):
        return 'static method called'
```

The `@staticmethod` decorator is a built-in decorator that defines a static method.

**When to use static methods?**

- When you need a utility function that doesn't access any properties of the class or its instances but logically
  belongs within the class.
- When you want to group functions related to the class for better code organization and readability, but these
  functions do not need to access class or instance-specific data.

**In summary, use a class method when you need to access or modify the state of the class, and use a static method when
you need a function that is related to the class but does not need to access or modify the class's state.**

<div style="background-color: antiquewhite; align-content: center">
<h3 style="color: red">My take:</h3>
  <p style="color: blue">Static methods are not useful at all!!</p>
</div>

## Private and Protected Attributes in Python

In Python there's no way to prevent someone from accessing an attribute (like private or protected modifier in Java).
However, there are some conventions that are
used to indicate that an attribute or method is intended to be private or protected.

- **Private attributes** are those that are intended to be used only inside the class definition. They are preceded by
  two underscores (`__`) and are not directly visible to outsiders. However, they can be accessed using name mangling.
  For
  example a `__mood` attribute in a class named `Person` will be accessible using `_Person__mood` from outside the
  class. If
  a `Student` class inherits from `Person`, the `__mood` attribute will be accessible using `_Student__mood`.

**Note:** Name mangling is not a security feature. It's just a convention to prevent accidental access to an attribute
that is intended to be used only inside the class definition. So it's more about safety than security.

- **Protected attributes**: Attributes with a single underscore (`_`) prefix are protected attributes. They are intended
  to be used only inside the class definition and in its subclasses. However, they are visible to outsiders and can be
  accessed directly. So, they are not really protected. They are just a convention to indicate that an attribute is
  intended to be used only inside the class definition and in its subclasses.

## Saving memory with __slots__

By default Python stores instance attributes in a per-instance `dict` named `__dict__`. This is really helpful as it
allows
you to add attributes to objects dynamically. However, it can also take up a lot of memory if you are creating a lot of
instances (millions) of a class that only has a few attributes. In this case, you can use the `__slots__` class
attribute.

The `__slots__` class attribute allows you to explicitly state which instance attributes you expect your object
instances
to have, and it will only allocate enough space in each instance to store the attributes listed in `__slots__`. Here is
an example:

```python
class MyClass:
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()

    def set_up(self):
        pass
```

In this example, we have defined a class named `MyClass` that has two instance attributes: `name` and `identifier`. We
have also defined a `__slots__` attribute that contains a list of the names of the attributes that we expect our object
instances to have. This will save a lot of memory if we are creating millions of instances of `MyClass`.

```python
>> > a = MyClass('name', 'id')
>> > a.name
'name'
>> > a.identifier
'id'
>> > a.__dict__
Traceback(most
recent
call
last):
File
"<stdin>", line
1, in < module >

```

A counterintuitive side effect of using `__slots__` is that it is only partially inherited by subclasses. This is
counterintuitive because you might expect subclasses to have the same `__slots__` as their parents, but this is not the
case. Only the attributes listed in the `__slots__` of a class will be reserved in the instances of that class. The
attributes of its parent classes are not reserved in its instances. Here is an example:

```python
class MyClass:
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()

    def set_up(self):
        pass


class MyChildClass(MyClass):
    pass

>> > a = MyChildClass('name', 'id')
>> > a.name
'name'
>> > a.identifier
'id'
>> > a.__dict__
{}
>> > a.other_variable = 'hello'
>> > a.other_variable
'hello'
>> > a.__dict__
{'other_variable': 'hello'}
```

<div style="color: cadetblue; font-weight: bold; font-size: medium">It is possible to *save memory and eat it too*: if 
you add `__dict__` name to the `__slots__` list. </div>



