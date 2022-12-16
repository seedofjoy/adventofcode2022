def parse_range(section_pairs):
    from_section, to_section = section_pairs.split("-")
    return int(from_section), int(to_section)


def contains(range_a, range_b):
    return range_a[0] <= range_b[0] and range_a[1] >= range_b[1]


def overlaps(range_a, range_b):
    return (
        range_b[0] <= range_a[0] <= range_b[1] or range_b[0] <= range_a[1] <= range_b[1]
    )


ranges = [
    (parse_range(ranges[0]), parse_range(ranges[1]))
    for line in open("input")
    if (ranges := line.strip().split(","))
]


def part_1():
    return sum(
        1
        for range_a, range_b in ranges
        if contains(range_a, range_b) or contains(range_b, range_a)
    )


def part_2():
    return sum(
        1
        for range_a, range_b in ranges
        if overlaps(range_a, range_b) or overlaps(range_b, range_a)
    )


print("Part 1:", part_1())
print("Part 2:", part_2())
