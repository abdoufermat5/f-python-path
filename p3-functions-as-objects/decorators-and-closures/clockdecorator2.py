import time

DEFAULT_FMT = "[{elapsed:0.8f}s] {name} ({args}) -> {result}"


class clock:

    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ", ".join(map(repr, _args))
            result = repr(_result)

            print(self.fmt.format(**locals()))
            return _result

        return clocked


@clock()
def snooze(seconds):
    time.sleep(seconds)
    return "Ok Abdou"


@clock(fmt='{name}({args}) takes {elapsed}s time to execute -> {result}')
def snooze2(seconds):
    time.sleep(seconds)
    return "Ok Abdel"


if __name__ == "__main__":
    for i in range(3):
        snooze(.123)

    for i in range(3):
        snooze2(.124)
