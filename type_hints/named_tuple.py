from typing import List, NamedTuple, Tuple

lst: List[int] = [1, 2, 3]
lst[0] = 2

t = (1, 2, 3)





def sample():

    # define a read-only map with typed name and id fields
    MyType = NamedTuple('MyType', [('name', str), ('id', int)])

    my_instance = MyType('Carsten', 10)

    # detects that ID is not a string
    my_invalid_instance = MyType('Carsten', '10')

    # knows that the identifier is an int
    identifier = my_instance.id

    # ok, since identifier is int
    y = identifier + 1


def sample1():

    # define a read-only map with typed name and id fields
    class MyType(NamedTuple):
        name: str
        id: int

    my_instance = MyType('Carsten', 10)

    # detects that ID is not a string
    my_invalid_instance = MyType('Carsten', '10')

    # knows that the identifier is an int
    identifier = my_instance.id

    # ok, since identifier is int
    y = identifier + 1
