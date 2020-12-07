"""https://adventofcode.com/2020/"""

from collections import Counter
import math
import re
import string
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


def bsp(lowers: List[bool]) -> int:
    """Binary space partitioning. Each input is whether we use lower."""
    low, high = 0, 2 ** len(lowers) - 1
    for l in lowers:
        delta = math.ceil((high - low) / 2)
        if l:
            high -= delta
        else:
            low += delta
    assert low == high
    return low


def seat(code: str) -> int:
    row = bsp([c == "F" for c in list(code)[:7]])
    col = bsp([c == "L" for c in list(code)[7:]])
    return row * 8 + col


def day_5_1() -> None:
    """BFFFBFBLRR"""
    print(max([seat(l) for l in get_lines("data/day_5.txt")]))


def day_5_2() -> None:
    seats = set([seat(l) for l in get_lines("data/day_5.txt")])
    for i in range(min(seats) + 1, max(seats)):
        if i not in seats:
            print(i)


def day_6_1() -> None:
    print(sum(len(set(x.replace("\n", ""))) for x in read("data/day_6.txt").split("\n\n")))


def day_6_2() -> None:
    cnt = 0
    for group in read("data/day_6.txt").split("\n\n"):
        yes = set(string.ascii_lowercase)
        for person in group.split("\n"):
            yes &= set(person)
        cnt += len(yes)
    print(cnt)


BagTree = Dict[str, Dict[str, int]]


def build_bag_tree() -> BagTree:
    d = {}
    for line in get_lines("data/day_7.txt"):
        chunks = line.split(" bags contain ")
        x = chunks[0]
        ys = chunks[1][:-1]
        ld = {}
        if ys != "no other bags":
            for y_phrase in ys.split(", "):
                n = int(y_phrase.split(" ")[0])
                y = " ".join(y_phrase.split(" ")[1:-1])
                ld[y] = n
        d[x] = ld
    return d


def day_7_1() -> None:
    """light olive bags contain 2 posh magenta bags, 4 dim crimson bags."""

    def check_bags(d: BagTree, key: str) -> bool:
        return "shiny gold" in d[key] or any(check_bags(d, k) for k in d[key].keys())

    d = build_bag_tree()
    print(sum(check_bags(d, k) for k in d.keys()))


def day_7_2() -> None:
    def sum_bags(d: BagTree, key: str) -> int:
        return sum(n * (1 + sum_bags(d, k)) for k, n in d[key].items())

    d = build_bag_tree()
    print(sum_bags(d, "shiny gold"))


def main() -> None:
    # day_1_1()
    # day_1_2()
    # day_2_1()
    # day_2_2()
    # day_3_1()
    # day_3_2()
    # day_4_1()
    # day_4_2()
    # day_5_1()
    # day_5_2()
    # day_6_1()
    # day_6_2()
    # day_7_1()
    day_7_2()


if __name__ == "__main__":
    main()
