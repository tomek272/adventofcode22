from collections import defaultdict
import matplotlib.pyplot as plt
import time

file = 'day09_input'


def solve(file_, part):

    def distance(pos1, pos2):
        return ((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)**0.5

    with open(file_) as f:
        motion = [m.strip('\n').split(' ') for m in f.readlines()]

    pos_h = [0., 0.]
    pos_t = [0., 0.]
    pos_t_counts = defaultdict(int)
    debug = False
    if debug:
        n, n_start, n_max = 0, 0, 10
        plt.ion()

    for direction, steps in motion: # d: direction, s: steps
        if debug:
            if n == n_max:
                break
            else:
                n += 1
                print(f'n: {n}')
                print(f'{direction} {steps}')

        for s in range(int(steps)):
            pos_h_last = pos_h[:] # remember last head position for potential diagonal tail move to follow
            pos_t_last = pos_t[:]

            ### move head
            if direction == 'R':
                pos_h[0] += 1
            elif direction == 'L':
                pos_h[0] -= 1
            elif direction == 'U':
                pos_h[1] += 1
            elif direction == 'D':
                pos_h[1] -= 1

            if debug:
                print(f'head: {pos_h}')

            ### move tail
            # exact 45 degree diagonal misalignment
            if distance(pos_h, pos_t) < 2 and not debug:
                pass
            # vertical or horizontal misalignment
            elif distance(pos_h, pos_t) == 2:
                # vertical misalignment
                if pos_h[0] == pos_t[0]:
                    pos_t[1] = pos_h[1] - (pos_h[1] - pos_t[1]) / 2
                # horizontal misalignment
                elif pos_h[1] == pos_h[1]:
                    pos_t[0] = pos_h[0] - (pos_h[0] - pos_t[0]) / 2
            # non-45-degree diagonal misalignment
            elif distance(pos_h, pos_t) > 2:
                pos_t = pos_h_last

            if debug:
                print(f'tail: {pos_t}')

            if debug and n >= n_start:
                time.sleep(0)
                plt.plot(*pos_h_last, 'b+')
                plt.plot(*pos_t_last, 'rx')
                plt.plot(*pos_h, 'b+', markersize=10.)
                plt.plot(*pos_t, 'rx', markersize=10.)
                plt.axis([-20, 20, -20, 20])
                plt.draw()
                plt.show()
                plt.pause(1)
                plt.clf()

            # print(f'head: {pos_h}, tail: {pos_t}')
            pos_t_counts[tuple(pos_t)] += 1

    return len(pos_t_counts)

if __name__ == '__main__':
    print('Solution to part one: ', solve(file_=file, part=1))
    # print('Solution to part two: ', solve(file_=file, part=2))