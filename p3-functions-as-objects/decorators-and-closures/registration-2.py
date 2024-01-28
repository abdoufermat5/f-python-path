registry = set()


def register(active=True):
    def decorate(func):
        print("running register"
              f"(active={active}) -> decorate({func})")
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func

    return decorate


@register(active=False)
def f1():
    print("running f1()")


@register(active=True)
def f2():
    print("running f2()")


@register()
def f3():
    print("running f3()")


def main():
    print('running main()')
    print('registry ->', registry)  # registry -> [<function f1 at 0x7f9b1c1b2d08>, <function f2 at 0x7f9b1c1b2d90>]
    # registry holds references to the two decorated functions
    f1()
    f2()
    f3()

    print("removing f3 from registry")
    # remove f3
    register(active=False)(f3)
    print('registry ->', registry)

    print("Adding f1 to registry")
    register(active=True)(f1)
    print('registry ->', registry)


if __name__ == "__main__":
    main()
