def part_1():
    calories = [0]
    for line in open("input"):
        cal = line.strip()
        if cal:
            calories[-1] += int(cal)
        else:
            calories.append(0)
    return max(calories)


def part_2():
    calories = [0]
    for line in open("input"):
        cal = line.strip()
        if cal:
            calories[-1] += int(cal)
        else:
            calories.append(0)
    return sum(sorted(calories)[-3:])


print("Part 1:", part_1())
print("Part 2:", part_2())
