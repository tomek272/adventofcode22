file = 'day03_input'


def calc_prio(letter: str):

    if letter.islower():
        return ord(letter) - 96

    elif letter.isupper():
        return ord(letter) - 38


def part_one(contents):

    with open(contents) as contents_:

        items = contents_.readlines()
        prio = 0

        for i in items:
            i.rstrip()
            n_i = int((len(i)) / 2)

            compartment1 = i[ : n_i]
            compartment2 = i[n_i : ]

            item_shared = list(
                set(compartment1) & set(compartment2)
            )
            prio += calc_prio(item_shared[0])

    return prio

def part_two(contents):

    with open(contents) as contents_:

        items = contents_.readlines()
        prio = 0

        for c, i in enumerate(items):
            i_ = [x for x in i if x.isalpha()]

            if (c+1) % 3 == 1:
                rucksack1 = i_

            if (c+1) % 3 == 2:
                rucksack2 = i_

            if (c+1) % 3 == 0:
                rucksack3 = i_

                item_shared = list(
                    set(rucksack1) & set(rucksack2) & set(rucksack3)
                )

                prio += calc_prio(item_shared[0])

    return prio


if __name__ == '__main__':
    print('Solution to part one: ', part_one(contents=file))
    print('Solution to part two: ', part_two(contents=file))