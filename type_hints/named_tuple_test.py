from typing import Dict, NamedTuple


def sample():

    class MyKey(NamedTuple):
        name: str
        id: int

    d: Dict[MyKey, str] = dict()

    key1 = MyKey('Carsten', 10)
    key2 = MyKey('Carsten', 20)

    d[key1] = 'value1'
    d[key2] = 'value2'

    print(d[key1])


if __name__ == '__main__':

    sample()