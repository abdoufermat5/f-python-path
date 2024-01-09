import builtins
from collections import ChainMap, UserDict
from types import MappingProxyType


# The main reason why it’s better to subclass UserDict rather than dict is
# that the built-in has some implementation shortcuts that end up forcing us to
# override methods that we can just inherit from UserDict with no problems.
class StrKeyDict1(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)

        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


class StrKeyDict2(UserDict):
    def __missing__(self, key):
        if isinstance(self, key):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return key in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value  # call to the default __getitem__ method


# Mutable Mapping

# The mapping types provided by the standard library are all mutable, but you
# may need to prevent users from changing a mapping by accident.

d = {"a": 5}
d_proxy = MappingProxyType(d)

# d_proxy is read-only but changes on d will be propagated and can be seen on d_proxy


# Views

# A view object is a dynamic proxy. If the source dict is updated, you can
# immediately see the changes through an existing view.

b = d.values()  # this creates a view of values in d
# b actually contains: 5
# a change in d will be propagated to the view object
d["j"] = 56


# now b contains: 5 and 56

# .keys(), .values(), .items() are all views


# Key sharing dict

class BaseClass:
    def __init__(self):
        self.attr1 = 'BaseClass attr1'


class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        self.attr2 = 'DerivedClass attr2'


if __name__ == '__main__':
    inst = BaseClass()
    inst3 = DerivedClass()
    value = inst3.attr1  # This will get the value of 'attr1' from the shared dictionary
    print("inst3.attr1", value)  # Output: BaseClass attr1

    print("BaseClass inst.__dict__", inst.__dict__)
    print("DerivedClass inst3.__dict__", inst3.__dict__)
