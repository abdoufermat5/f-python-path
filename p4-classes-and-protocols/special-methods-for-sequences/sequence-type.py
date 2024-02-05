class Foo:

    def __init__(self):
        self.baz = "baz is OK"

    def __getattr__(self, name):
        return name

    def __len__(self):
        return 42

    def __getitem__(self, pos):
        return pos


if __name__ == '__main__':
    f = Foo()
    print(len(f))  # calls f.__len__() method
    print(f[1:4:2])  # slice(1, 4, 2) is passed to __getitem__ method
    print(f[1])  # 1 is passed to __getitem__ method
    print(f[1:4])  # slice(1, 4, None) is passed to __getitem__ method

    print(f.baz)  # baz
    print(f.bar)  # bar