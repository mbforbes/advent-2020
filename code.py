"""https://adventofcode.com/2020/"""

from collections import Counter
import math
import typing
from typing import List, Tuple, Set, Dict, Any, Optional, NamedTuple, Iterator, Union

import IPython
from mbforbes_python_utils import read


def day_1_1() -> None:
    nums = [int(x) for x in read('data/day_1.txt').split("\n")]
    for i in nums:
        for j in nums:
            if i + j == 2020:
                print(i*j)
                return

def day_1_2() -> None:
    nums = [int(x) for x in read('data/day_1.txt').split("\n")]
    for i in nums:
        for j in nums:
            for k in nums:
                if i + j + k == 2020:
                    print(i*j*k)
                    return

def day_2_1() -> None:
    """
    10-15 w: wmwlwwwwfgwwjrzwwwww
    """
    n_valid = 0
    for line in [l.strip() for l in read("data/day_2.txt").split("\n")]:
        # print(f"Line: {line}")
        chunks = line.split(" ")
        min_, max_ = [int(x) for x in chunks[0].split("-")]
        letter = chunks[1][0]
        pwd = chunks[2]
        # print("Min:", min_)
        # print("Max:", max_)
        # print("Letter:", letter)
        # print("Pwd:", pwd)
        cnt: typing.Counter[str] = Counter(pwd)
        if cnt[letter] >= min_ and cnt[letter] <= max_:
            n_valid += 1
    print(n_valid)


def day_2_2() -> None:
    n_valid = 0
    for line in [l.strip() for l in read("data/day_2.txt").split("\n")]:
        chunks = line.split(" ")
        pos1, pos2 = [int(x) for x in chunks[0].split("-")]
        letter = chunks[1][0]
        pwd = chunks[2]
        if sum([pwd[pos1-1] == letter, pwd[pos2-1] == letter]) == 1:
            n_valid += 1
    print(n_valid)


def lines(path: str) -> List[str]:
    return [l.strip() for l in read(path).split("\n")]


def day_3_1() -> None:
    """
    ..##.......
    #...#...#..
    .#....#..#.
    """
    n_trees = 0
    global_x = 0
    for line in lines("data/day_3.txt"):
        local_x = global_x % len(line)
        if line[local_x] == "#":
            n_trees += 1
        global_x += 3
    print(n_trees)


def check_slope(slope: List[str], right: int, skip: bool) -> int:
    n_trees = 0
    global_x = 0
    skip_next = False
    for line in slope:
        # hack for y slope of 2
        if skip_next:
            skip_next = skip and (not skip_next)
            continue
        local_x = global_x % len(line)
        if line[local_x] == "#":
            n_trees += 1
        global_x += right
        skip_next = skip and (not skip_next)
    return n_trees


def day_3_2() -> None:
    """
    ..##.......
    #...#...#..
    .#....#..#.
    """
    slope = lines("data/day_3.txt")
    print(math.prod([
        check_slope(slope, 1, False),
        check_slope(slope, 3, False),
        check_slope(slope, 5, False),
        check_slope(slope, 7, False),
        check_slope(slope, 1, True),
    ]))


def main() -> None:
    # day_1_1()
    # day_1_2()
    # day_2_1()
    # day_2_2()
    # day_3_1()
    day_3_2()


if __name__ == "__main__":
    main()
