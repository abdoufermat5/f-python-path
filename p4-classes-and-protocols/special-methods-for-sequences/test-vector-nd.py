from VectorND import VectorND

if __name__ == '__main__':
    v10 = VectorND(range(10))
    print(v10)
    print(v10[1:4])
    print(v10[1:4][0])
    print(v10[-1])
    print(v10[1:4][1:2])
    # print(v10[1, 3])  # TypeError: __getitem__ only accepts slices or integers as index
    print(v10.x, v10.y, v10.z)  # 0 1 2
    print(v10.t)  # 3
    print(v10.baz)  # "VectorND" object has no attribute "baz"
