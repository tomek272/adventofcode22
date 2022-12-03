file = 'day02_input'


def translate_hand(hand):

    hand_translation = {
        'A': 'rock', 'X': 'rock',
        'B': 'paper', 'Y': 'paper',
        'C': 'scissors', 'Z': 'scissors',
    }

    return hand_translation[hand]


def translate_order(order):

    order_translation = {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win',
    }

    return order_translation[order]


def find_your_hand(hand_opp, order):

    if hand_opp == 'rock':
        hands = {
            'lose': 'scissors',
            'draw': 'rock',
            'win': 'paper',
        }
        return hands[order]

    elif hand_opp == 'paper':
        hands = {
            'lose': 'rock',
            'draw': 'paper',
            'win': 'scissors',
        }
        return hands[order]

    elif hand_opp == 'scissors':
        hands = {
            'lose': 'paper',
            'draw': 'scissors',
            'win': 'rock',
        }
        return hands[order]


def calc_points(hand_opp, hand_me):

    if hand_me == 'rock':
        points = 1
        if hand_opp == 'rock':
            points += 3
        elif hand_opp == 'paper':
            points += 0
        elif hand_opp == 'scissors':
            points += 6

    elif hand_me == 'paper':
        points = 2
        if hand_opp == 'rock':
            points += 6
        elif hand_opp == 'paper':
            points += 3
        elif hand_opp == 'scissors':
            points += 0

    elif hand_me == 'scissors':
        points = 3
        if hand_opp == 'rock':
            points += 0
        elif hand_opp == 'paper':
            points += 6
        elif hand_opp == 'scissors':
            points += 3

    return points


def part_one(strategy):

    with open(strategy) as s:

        duels = s.readlines()
        points = 0

        for d in duels:
            hand_opp = translate_hand(d[0])
            hand_me = translate_hand(d[-2])

            points += calc_points(hand_opp, hand_me)

    return points

def part_two(strategy):

    with open(strategy) as s:

        duels = s.readlines()
        points = 0

        for d in duels:
            hand_opp = translate_hand(d[0])
            hand_me = find_your_hand(translate_hand(d[0]), translate_order(d[-2]))

            points += calc_points(hand_opp, hand_me)

    return points



if __name__ == '__main__':
    print('Solution to part one: ', part_one(strategy=file))
    print('Solution to part two: ', part_two(strategy=file))