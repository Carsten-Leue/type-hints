
from typing import Union


class MyClass(object):

    def __init__(self) -> None:
        # declares the type of x
        self.x: Union[int, str] = 10

    def do_sth(self) -> int:
        # ok, x is of type int
        return self.x + 10
