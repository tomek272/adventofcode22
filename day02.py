file = 'day02_input'


def translate_hand():

    # Todo: translate hand from 'abc' or 'xyz' to 'rock', 'paper', 'sciccors'

    pass


def find_your_hand():

    # Todo: find your hand according to order


def calc_points(hand_opp, hand_me):

    # Todo: receive hands 'rock', 'paper', 'sciccors'

    if hand_me == 'X': # rock
        points = 1
        if hand_opp == 'A': # rock
            points += 3
        elif hand_opp == 'B': # paper
            points += 0
        elif hand_opp == 'C': # sciccors
            points += 6

    elif hand_me == 'Y': # paper
        points = 2
        if hand_opp == 'A': # rock
            points += 6
        elif hand_opp == 'B': # paper
            points += 3
        elif hand_opp == 'C': # sciccors
            points += 0

    elif hand_me == 'Z': # scissors
        points = 3
        if hand_opp == 'A': # rock
            points += 0
        elif hand_opp == 'B': # paper
            points += 6
        elif hand_opp == 'C': # sciccors
            points += 3

    return points


def part_one(strategy):

    with open(strategy) as s:

        duels = s.readlines()
        points = 0

        for d in duels:
            hand_opp = d[0]
            hand_me = d[-2]

            points += calc_points(hand_opp, hand_me)

    return points

if __name__ == '__main__':
    print('Solution to part one: ', part_one(strategy=file))