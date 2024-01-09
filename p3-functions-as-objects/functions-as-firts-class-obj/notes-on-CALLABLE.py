import random


class BingoCage:
    def __init__(self, items):
        self.items = list(items)
        random.shuffle(self.items)

    def pick(self):
        try:
            return self.items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")

    def __call__(self):
        return self.pick()


def execute_bc():
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))


def tag(name, *content, class_=None, **attrs):
    """Generates one or more HTML tags"""

    if class_ is not None:
        attrs["class"] = class_

    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = "".join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)

        return "\n".join(elements)
    else:
        return f'<{name}{attr_str}/>'


def execute_t():
    header = tag('div', "login", "logout", "contact us", class_="head", style="padding: 10px;")
    print(header)
    img = {"name": "img", "src": "images/pic.jpg", "alt": "sky is beautiful", "width": "100%", "class": "skiImg"}
    print(tag(**img))


def factorial(n):
    from functools import reduce
    from operator import mul

    return reduce(mul, range(1, n + 1))


def operators_in_action():
    from operator import itemgetter, attrgetter
    from collections import namedtuple
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    sorted_metro_data = sorted(metro_data, key=itemgetter(1))
    print(sorted_metro_data)
    LatLon = namedtuple("LatLo", "lat lon")
    Metropolis = namedtuple("Metropolis", "name cc pop coord")
    metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon)) for name, cc, pop, (lat, lon) in metro_data]

    print("\nlist of cities:\n ", *metro_areas, sep="\n-->\t")
    print("\n\nattrgetter in action:\n")
    name_lat = attrgetter("name", "coord.lat")
    for city in sorted(metro_areas, key=attrgetter("coord.lat")):
        print(name_lat(city))


def partial_in_action():
    from operator import mul
    from functools import partial

    triple = partial(mul, 3)  # 3 become the first argument of mul, the other is filled when triple is called!
    triple(7)  # 7 becomes the second argument of mul so output: 7*3 = 21
    triples = list(map(triple, range(11)))
    print(triples)


if __name__ == "__main__":
    partial_in_action()
