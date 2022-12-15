def part_1():
    won_table = {
        "B X": 1,
        "C Y": 2,
        "A Z": 3,
        "A X": 4,
        "B Y": 5,
        "C Z": 6,
        "C X": 7,
        "A Y": 8,
        "B Z": 9,
    }
    return sum(won_table[l.strip()] for l in open("input"))


def part_2():
    indices_map = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
    shape_scores = (1, 2, 3)
    result_scores = (0, 3, 6)

    rotates = (-1, 0, 1)

    score = 0
    for l in open("input"):
        (opponent, result) = l.strip().split(" ")
        opponent_idx = indices_map[opponent]
        result_idx = indices_map[result]

        my_idx = (opponent_idx + rotates[result_idx]) % 3
        score += shape_scores[my_idx] + result_scores[result_idx]

    return score


print("Part 1:", part_1())
print("Part 2:", part_2())
