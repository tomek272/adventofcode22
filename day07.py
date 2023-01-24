file = 'day07_input'
# TODO: where's the error, copied it from here https://www.reddit.com/r/adventofcode/comments/zesk40/2022_day_7_solutions/
from collections import defaultdict

def get_filesizes(file):
    with open(file) as f:
        lines_ = list(f.readlines())

    lines = [l for l in lines_ if l != '$ ls']
    filepath = []
    sizes = defaultdict(int)

    for line in lines:
        if line.startswith('$ cd'):
            match line:
                case '$ cd /':
                    filepath.clear()
                    filepath.append('/')
                case '$ cd ..':
                    filepath.pop()
                case _:
                    dir = line.split()[-1]
                    filepath.append(dir)

        else:
            filesize = line.split()[0]
            if filesize.isdigit():
                for i in range(len(filepath)):
                    dir = '/'.join(filepath[:i + 1]).replace("//", "/")
                    sizes[dir] = int(filesize)

    return sizes


def main():

    # Part one
    sizes = get_filesizes(file=file)
    # print(sizes)
    dirs_below_threshold = {directory: size for (directory, size) in sizes.items() if size <= 100000}

    print('Solution to part one: ', sum(dirs_below_threshold.values()))

    # Part two




if __name__ == '__main__':
    main()