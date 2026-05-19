from typing import Any


def mode(input_list: list) -> list[Any]:
    """This function returns the mode(Mode as in the measures of
    central tendency) of the input data.

    The input list may contain any Datastructure or any Datatype.

    >>> mode([2, 3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 2, 2, 2])
    [2]
    >>> mode([3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 2, 2, 2])
    [2]
    >>> mode([3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 4, 2, 2, 4, 2])
    [2, 4]
    >>> mode(["x", "y", "y", "z"])
    ['y']
    >>> mode(["x", "x" , "y", "y", "z"])
    ['x', 'y']
    """
    if not input_list:
        return []
    counts: dict[Any, int] = {}
    for value in input_list:
        counts[value] = counts.get(value, 0) + 1
    max_count = max(counts.values())
    return sorted(value for value, count in counts.items() if count == max_count)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
