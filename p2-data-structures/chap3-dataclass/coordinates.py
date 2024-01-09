import typing

from typing import NamedTuple
from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


# weird things
# issubclass(Coordinate, typing.NamedTuple) return False
# issubclass(Coordinate, tuple) return True
if __name__ == '__main__':
    print(issubclass(Coordinate, typing.NamedTuple))
    print(issubclass(Coordinate, tuple))
    print(Coordinate.__annotations__)
    print(Coordinate.__dict__)
