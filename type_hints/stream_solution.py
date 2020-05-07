from tempfile import gettempdir
from pathlib import Path
from typing import IO, Protocol, cast


def sample():

    class Writable(Protocol):

        def write(self, s: str) -> int:
            ...

    def writer(dst: Writable) -> None:
        dst.write('Hallo World!')

    filename = Path(gettempdir()).joinpath('test.log')

    with open(filename, 'w') as fp:
        writer(fp)


if __name__ == '__main__':

    sample()
