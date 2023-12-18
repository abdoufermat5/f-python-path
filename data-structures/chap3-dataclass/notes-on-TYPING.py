import typing
from dataclasses import dataclass, field


class Coordinate(typing.NamedTuple):
    lat: float
    lon: float


class DemoPlainClass:
    a: int  # becomes an entry in __annotations__ but no attributes named "a" is created in the class
    b: float = 1.2  # becomes an entry in __annotations__ and an attributes named "b" with value 1.2 is created
    c = "bwahahaha"  # is just a plain old class attribute, not an annotation


class DemoNTClass(typing.NamedTuple):
    a: int
    b: float = 1.2
    c = "bwahhaha"


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.2
    c = "bwahhaha"


@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)  # this ensures each instance has its own members list


@dataclass
class HackerClubMember(ClubMember):
    all_handles: typing.ClassVar[set[str]] = set()  # is a class attributes
    handle: str = ""

    def __post_init__(self):
        cls = self.__class__  # get the class of the instance
        if self.handle == "":
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f"handle {self.handle!r} already exists."
            raise ValueError(msg)
        cls.all_handles.add(self.handle)


if __name__ == '__main__':
    test = Coordinate("bwahahah", None)
    print(test)
    print("-" * 20)
    print(DemoPlainClass.__annotations__)
    try:
        print(DemoPlainClass.a)
    except AttributeError as a:
        print("Error", a)
        # Error type object 'DemoPlainClass' has no attribute 'a'
    print("-" * 20)
    print(DemoNTClass.__annotations__)
    try:
        print(DemoNTClass.a)
    except AttributeError as a:
        print("Error", a)

    print(DemoNTClass.__doc__)

    print("-"*20)

    try:
        print(DemoDataClass.a)
    except AttributeError as ae:
        print("Error ", ae)  # no error is raised
    print(DemoDataClass.__doc__)

    print("-" * 20)
    print(ClubMember.__doc__)
    print("-" * 20)
    print(HackerClubMember.__doc__)
