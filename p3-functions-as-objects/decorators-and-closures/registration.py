registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)  # registry -> [<function f1 at 0x7f9b1c1b2d08>, <function f2 at 0x7f9b1c1b2d90>]
    # registry holds references to the two decorated functions
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
