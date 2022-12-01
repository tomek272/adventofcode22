file = 'input'


def part_one(calories_list):
    with open(calories_list) as f:

        lines = f.readlines()
        elves = []
        calories = 0

        for l in lines:
            try:
                calories += int(l)
            except:
                elves.append(calories)
                calories = 0

    return elves


def part_two(elves, n=3):
    elves.sort()
    return sum(elves[-n:])


if __name__ == "__main__":
    calories_per_elf = part_one(file)

    print("Solution to part one: ", max(calories_per_elf))
    print("Solution to part two: ", part_two(calories_per_elf))
