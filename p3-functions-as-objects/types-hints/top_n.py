from typing import TypeVar, Iterable, List, Protocol

T = TypeVar('T')


def top(series: Iterable[T], length: int) -> List[T]:
    return sorted(series, reverse=True)[:length]


class SupportLessThan(Protocol):
    def __lt__(self, other: T) -> bool:
        ...


LT = TypeVar('LT', bound=SupportLessThan)


def top_2(series: Iterable[LT], length: int) -> List[LT]:
    return sorted(series, reverse=True)[:length]


if __name__ == '__main__':
    test = [5, 0, 1, 54, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_2 = ["apple", "banana", "honeydew", "indigo", "jackfruit", "cherry", "durian", "eggplant", "fig", "grape"]
    print(top(test_2, 5))

    test3 = [object() for _ in range(10)]
    print(top_2(test3, 5))  # type hint detects that object() does not support < operator
    print(top_2(test, 5))   # type hint detects that int does support < operator
