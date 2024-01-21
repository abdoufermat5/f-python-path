from collections import abc

from typing import List, Tuple, Union


def columnize(sequence: Union[List[str], Tuple[str]], num_columns: int = 0) -> List[Tuple[str, ...]]:
    if num_columns == 0:
        num_columns = round(len(sequence) ** 0.5)

    num_rows, remainder = divmod(len(sequence), num_columns)
    num_rows += bool(remainder)

    return [tuple(sequence[i::num_rows]) for i in range(num_rows)]


if __name__ == '__main__':
    animals = ['bear', 'cat', 'dog', 'elephant', 'fox', 'giraffe', 'hippopotamus', 'ibex', 'jackal', 'kangaroo', 'lion',
               'moose', 'nematode', 'orangutan', 'porcupine', 'quokka', 'rat', 'snake', 'tiger', 'unicorn', 'vulture',
               'whale', 'xiphias', 'yak', 'zebra']
    table = columnize(animals)
    for row in table:
        print(*row, sep='\t')

