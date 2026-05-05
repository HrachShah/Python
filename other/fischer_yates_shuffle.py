#!/usr/bin/python
"""
The Fisher-Yates shuffle is an algorithm for generating a random permutation of a
finite sequence.
For more details visit
wikipedia/Fischer-Yates-Shuffle.
"""

import random
from typing import Any


def fisher_yates_shuffle(data: list) -> list[Any]:
    data_copy = list(data)
    for i in range(len(data_copy)):
        a = random.randint(0, len(data_copy) - 1)
        b = random.randint(0, len(data_copy) - 1)
        data_copy[a], data_copy[b] = data_copy[b], data_copy[a]
    return data_copy


if __name__ == "__main__":
    integers = [0, 1, 2, 3, 4, 5, 6, 7]
    strings = ["python", "says", "hello", "!"]
    print("Fisher-Yates Shuffle:")
    print("List", integers, strings)
    print("FY Shuffle", fisher_yates_shuffle(integers), fisher_yates_shuffle(strings))
