from functools import singledispatch
from collections import abc

import fractions
import decimal
import html
import numbers


# singledispatch marks the base function that handles the object type.
@singledispatch
def htmlize(obj: object) -> str:
    content = html.escape(repr(obj))
    return f"<pre>{content}</pre>"


# each specialized function is decorated with the <base function>.register(<type>) decorator.
@htmlize.register
def _(text: str) -> str:
    content = html.escape(text).replace("\n", "<br/>\n")
    return f"<p>{content}</p>"


@htmlize.register
def _(seq: abc.Sequence) -> str:
    inner = "</li>\n<li>".join(htmlize(item) for item in seq)
    return "<ul>\n<li>" + inner + "</li>\n</ul>"


@htmlize.register
def _(n: numbers.Integral) -> str:
    return f"<pre>{n} (0x{n:x})</pre>"


@htmlize.register
def _(n: bool) -> str:
    return f"<pre>{n}</pre>"


@htmlize.register(fractions.Fraction)
def _(x) -> str:
    frac = fractions.Fraction(x)
    return f"<pre>{frac.numerator}/{frac.denominator}</pre>"


# the <base function>.register(<type>) decorator returns the undecorated function, so it's possible to stack decorators
# to register two or more types on the same implementation.
@htmlize.register(decimal.Decimal)
@htmlize.register(float)
def _(x) -> str:
    frac = fractions.Fraction(x).limit_denominator()
    return f"<pre>{x} ({frac.numerator}/{frac.denominator})</pre>"
