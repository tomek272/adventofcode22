file = 'day04_input'


def create_set(assignment_range):

    range_min, range_max = [int(i) for i in assignment_range.split('-')]
    return set(range(range_min, range_max+1))


def part_one(assignments):

    with open(assignments) as assignements_:

        assignment = assignements_.readlines()
        n = 0

        for a in assignment:
            a1, a2 = a.split(',')
            a1_set = create_set(a1)
            a2_set = create_set(a2)

            if a1_set.issubset(a2_set) or a2_set.issubset(a1_set):
                n += 1

    return n


def part_two(assignments):

    with open(assignments) as assignements_:

        assignment = assignements_.readlines()
        n = 0

        for a in assignment:
            a1, a2 = a.split(',')
            a1_set = create_set(a1)
            a2_set = create_set(a2)

            if len(a1_set & a2_set) > 0:
                n += 1

    return n


if __name__ == '__main__':
    print('Solution to part one: ', part_one(assignments=file))
    print('Solution to part two: ', part_two(assignments=file))