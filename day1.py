from collections import Counter

def part1(location_ids):
    """Given a list of pairs, sort the columns, and then get the difference beween each row"""
    lefts = [ int(left) for (left, right) in location_ids ]
    rights = [ int(right) for (left, right) in location_ids ]

    lefts.sort()
    rights.sort()

    return sum([ abs(left - right) for (left, right) in zip(lefts, rights) ])


def part2(location_ids):
    """Given a list of pairs, for each element on the left, see how often that occurs on the right.
    Then take the sum of products"""
    lefts = [ int(left) for (left, right) in location_ids ]
    rights = Counter([ int(right) for (left, right) in location_ids ])
    return sum([ left * rights[left] for left in lefts])


def read_input():
    with open("inputs/day1.txt") as f:
        return [ l.split() for l in f.readlines() ]


def main():
    day_input = read_input()
    print(part1(day_input))
    print(part2(day_input))


if __name__ == '__main__':
    main()
