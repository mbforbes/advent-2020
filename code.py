"""https://adventofcode.com/2020/"""

from collections import Counter
import math
import re
import typing
from typing import List, Tuple, Set, Dict, Any, Optional, NamedTuple, Iterator, Union

import IPython
from mbforbes_python_utils import read


def get_lines(path: str) -> List[str]:
    return [l.strip() for l in read(path).split("\n")]


def day_1_1() -> None:
    nums = [int(x) for x in get_lines("data/day_1.txt")]
    for i in nums:
        for j in nums:
            if i + j == 2020:
                print(i * j)
                return


def day_1_2() -> None:
    nums = [int(x) for x in get_lines("data/day_1.txt")]
    for i in nums:
        for j in nums:
            for k in nums:
                if i + j + k == 2020:
                    print(i * j * k)
                    return


def day_2_1() -> None:
    """
    10-15 w: wmwlwwwwfgwwjrzwwwww
    """
    n_valid = 0
    for line in get_lines("data/day_2.txt"):
        chunks = line.split(" ")
        min_, max_ = [int(x) for x in chunks[0].split("-")]
        letter = chunks[1][0]
        pwd = chunks[2]
        n_valid += 1 if Counter(pwd)[letter] in range(min_, max_ + 1) else 0
    print(n_valid)


def day_2_2() -> None:
    n_valid = 0
    for line in [l.strip() for l in read("data/day_2.txt").split("\n")]:
        chunks = line.split(" ")
        pos1, pos2 = [int(x) for x in chunks[0].split("-")]
        letter = chunks[1][0]
        pwd = chunks[2]
        n_valid += 1 if sum([pwd[pos1 - 1] == letter, pwd[pos2 - 1] == letter]) == 1 else 0
    print(n_valid)


def day_3_1() -> None:
    """
    ..##.......
    #...#...#..
    .#....#..#.
    """
    n_trees = 0
    global_x = 0
    for line in get_lines("data/day_3.txt"):
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
    slope = get_lines("data/day_3.txt")
    print(
        math.prod(
            [
                check_slope(slope, 1, False),
                check_slope(slope, 3, False),
                check_slope(slope, 5, False),
                check_slope(slope, 7, False),
                check_slope(slope, 1, True),
            ]
        )
    )


def day_4_1() -> None:
    """
    byr:2004

    hcl:#602927 iyr:2018 byr:1938 ecl:blu
    """
    n_valid = 0
    req_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for person in read("data/day_4.txt").split("\n\n"):
        keys = set([x.split(":")[0] for x in person.replace("\n", " ").split(" ")])
        n_valid += 1 if keys.issuperset(req_fields) else 0
    print(n_valid)


def day_4_2() -> None:
    def height(s: str) -> bool:
        if re.fullmatch("\d{2,3}(in|cm)", s) is None:
            return False
        if s[-2:] == "cm":
            return int(s[:-2]) in range(150, 194)
        return int(s[:-2]) in range(59, 76)  # s[-2:] == "in"

    req_fields = {
        "byr": lambda s: re.fullmatch("\d{4}", s) is not None and int(s) in range(1920, 2003),
        "iyr": lambda s: re.fullmatch("\d{4}", s) is not None and int(s) in range(2010, 2021),
        "eyr": lambda s: re.fullmatch("\d{4}", s) is not None and int(s) in range(2020, 2031),
        "hgt": height,
        "hcl": lambda s: re.fullmatch("#[0-9a-f]{6}", s) is not None,
        "ecl": lambda s: s in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": lambda s: re.fullmatch("[0-9]{9}", s) is not None,
    }

    n_valid = 0
    for person in read("data/day_4.txt").split("\n\n"):
        data = {x.split(":")[0]: x.split(":")[1] for x in person.replace("\n", " ").split(" ")}
        if not set(data.keys()).issuperset(req_fields):
            continue
        if sum([v(data[k]) for k, v in req_fields.items()]) == len(req_fields):
            n_valid += 1

    print(n_valid)


def main() -> None:
    # day_1_1()
    # day_1_2()
    # day_2_1()
    # day_2_2()
    # day_3_1()
    # day_3_2()
    # day_4_1()
    day_4_2()


if __name__ == "__main__":
    main()
