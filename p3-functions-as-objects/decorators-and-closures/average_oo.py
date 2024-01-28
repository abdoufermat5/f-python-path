class Average:

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


if __name__ == "__main__":
    print("Using Average class")
    avg = Average()
    print(avg(10))  # 10.0
    print(avg(11))  # 10.5
    print(avg(12))  # 11.0

    print("Using make_averager")
    avg2 = make_averager()
    print(avg2(10))  # 10.0
    print(avg2(11))  # 10.5
    print(avg2(12))  # 11.0
