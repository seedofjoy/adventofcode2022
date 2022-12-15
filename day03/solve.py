import string

PRIORITIES = {
    letter: i
    for letter, i in zip(string.ascii_letters, range(1, len(string.ascii_letters) + 1))
}


def grouper(iterable):
    return zip(*[iter(iterable)] * 3)


def part_1():
    priorities_sum = 0
    for line in open("input"):
        line = line.strip()
        a, b = line[: len(line) // 2], line[len(line) // 2 :]
        letter = set(a).intersection(b).pop()
        priorities_sum += PRIORITIES[letter]
    return priorities_sum


def part_2():
    priorities_sum = 0
    for lines in grouper(open("input")):
        letter = (
            set(lines[0].strip())
            .intersection(lines[1].strip())
            .intersection(lines[2].strip())
        ).pop()
        priorities_sum += PRIORITIES[letter]
    return priorities_sum


print("Part 1:", part_1())
print("Part 2:", part_2())
