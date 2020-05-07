from tempfile import gettempdir
from pathlib import Path
from typing import IO


def sample():

    def writer(dst: IO[str]) -> None:
        dst.write('Hallo')

    filename = Path(gettempdir()).joinpath('test.log')

    with open(filename, 'w') as fp:
        writer(fp)


if __name__ == '__main__':

    sample()
