from typing import List


def fibonacci_sequence(number: int) -> List[int]:
    sequence = [0, 1]

    for _ in range(number - 2):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def locate_number(number: int, sequence: List[int]) -> int or str:
    return sequence.index(number)
