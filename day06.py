file = 'day06_input'


def find_marker(stream, packet_len):
    for n in range(packet_len, len(stream)):
        packet = stream[n-packet_len : n]
        if len(set(packet)) == packet_len:
            return n


def solution(file_, part):

    with open(file_) as f:

        stream = f.readlines()[0]

        if part == 1:
            return find_marker(stream, 4)

        if part == 2:
            return find_marker(stream, 14)


    # return line


if __name__ == '__main__':
    print('Solution to part one: ', solution(file_=file, part=1))
    print('Solution to part two: ', solution(file_=file, part=2))