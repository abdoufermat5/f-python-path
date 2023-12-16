def check_immutability(obj):
    try:
        hash(obj)
    except TypeError:
        return False
    return True


if __name__ == '__main__':
    t = (1, 2, 3)
    print(check_immutability(t))   # True because tuple is immutable and all its elements are immutable
    t = ([1, 2, 3], [4, 5, 6])
    print(check_immutability(t))   # False because even though tuple is immutable, its elements are mutable
