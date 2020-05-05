
from typing import Protocol, Union


class MyFirstClass(object):

    def print(self) -> None:
        print('first')

    def first(self) -> None:
        pass


class MySecondClass(object):

    def print(self) -> None:
        print('second')

    def second(self) -> None:
        pass


def printer(out: Union[MyFirstClass, MySecondClass]) -> None:
    out.print()

# duck typing class for the print method


class Printable(Protocol):

    def print(self) -> None:
        pass


def better_printer(out: Printable) -> None:
    out.print()


if __name__ == '__main__':

    f = MyFirstClass()
    s = MySecondClass()

    printer(f)
    printer(s)

    better_printer(f)
    better_printer(s)
    
