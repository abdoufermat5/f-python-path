from typing import Union, Optional


def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}s'


def order(item: str, qty: Union[int, str]) -> str:
    if isinstance(qty, str):
        qty = int(qty)
    return f'{qty} {item}s'


