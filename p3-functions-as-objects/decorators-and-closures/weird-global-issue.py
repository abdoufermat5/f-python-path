b = 5


def f(a):
    print(a)
    print(b)  # UnboundLocalError: local variable 'b' referenced before assignment
    b = 9


def g(a):
    global b
    print(a)
    print(b)
    b = 9


if __name__ == "__main__":
    # f(3)
    print("b value", b)
    print("first call to g")
    g(3)
    # output: 3 5
    print("second call to g")
    g(3)
    # output: 3 9 because b is now 9
