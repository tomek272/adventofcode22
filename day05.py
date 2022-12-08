file = 'day05_input'


def solution(file_, part):

    with open(file_) as f:

        lines = f.readlines()

        l_starting_stacks = range(8)
        stacks = [[] for i in range(9)]

        l_crate_arrangements = range(10, 515+1)

        for i, line in enumerate(lines):

            # Read out stacks
            if i in l_starting_stacks:

                stack_level = line[1:34:4]

                for k, crate in enumerate(stack_level):
                    if crate.isalpha():
                        stacks[k].append(crate)

            # Arrange stacks
            if i in l_crate_arrangements:

                _, n, _, source, _, target = line.split(' ')

                if part == 1:
                    # Arrange multiple crates crate by crate (i.e. reversing order)
                    for n_ in range(int(n)):
                        stacks[int(target)-1].insert(0, stacks[int(source)-1].pop(0))

                if part == 2:
                    # Arrange multiple crates all at once (i.e. keeping order)
                    crates = stacks[int(source) - 1][:int(n)]
                    stacks[int(source) - 1] = stacks[int(source) - 1][int(n):]
                    stacks[int(target) - 1] = crates + stacks[int(target)-1]


    return ''.join([s[0] for s in stacks])


if __name__ == '__main__':
    print('Solution to part one: ', solution(file_=file, part=1))
    print('Solution to part two: ', solution(file_=file, part=2))