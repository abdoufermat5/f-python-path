from functools import singledispatch


@singledispatch
def base_func(arg):
    print(f"base_func({arg!r})")


@base_func.register
def _(arg: int):
    print(f"base_func({arg!r}) is an int")


@base_func.register
def _(arg: list):
    print(f"base_func({arg!r}) is a list")


@base_func.register(complex)
def _(arg: complex):
    print(f"base_func({arg!r}) is a complex")


if __name__ == '__main__':
    base_func(1)
    base_func([1, 2, 3])
    base_func(1.0)
    base_func(1 + 1j)
    base_func("1")