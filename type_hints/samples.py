from typing import List, Set, Dict, Tuple, Optional, Union

# simple function

IntOrStr = Union[int, str]


def my_method(x: Optional[int]) -> None:
    pass


my_method(None)
my_method(1)
my_method('None')


def add(x: int, y: int) -> int:
    return x + y


def sample1():

    # x is automatically detected to be int
    x = add(1, 2)

    # ok
    y = x + 1


def sample2():

    list: List[str] = []

    # cannot append an int to a list of strings
    list.append(1)


def sample3():

    IntOrString = Union[int, str]
    list: List[IntOrString] = list()

    # append heterogenous types
    list.append(1)
    list.append('test')

    # but not bytes
    list.append(b'abc')
