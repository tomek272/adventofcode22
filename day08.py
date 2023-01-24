file = 'day08_input'


def solve(file_, part):

    with open(file_) as f:
        grid = list(f)
    grid = [[int(tree) for tree in row.strip('\n')] for row in grid]

    n_visible = 0
    n_invisible = 0

    if part == 1:

        for i, row in enumerate(grid):

            if (i == 0) or (i == len(grid) - 1):
                n_visible += len(grid)
                continue

            for j, tree in enumerate(row):

                if (j == 0) or (j == len(row) - 1):
                    n_visible += 1
                    continue
                elif (tree > max(row[:j])) or (tree > max(row[j+1:])) or (tree > max([row_[j] for row_ in grid][:i])) or (tree > max([row_[j] for row_ in grid][i+1:])):
                    n_visible += 1
                    continue
                else:
                    n_invisible += 1

        if (n_visible + n_invisible) != ((i+1) * (j+1)):
            print(f'Error: counted in total {n_visible + n_invisible} trees instead of {(i+1) * (j+1)}')

        return n_visible

    if part == 2:

        highscore = 0

        for i, row in enumerate(grid):

            for j, own_tree in enumerate(row):

                l_score, r_score, u_score, d_score = 0, 0, 0, 0

                for other_tree in row[:j][::-1]:

                    if other_tree < own_tree:
                        l_score += 1
                    elif other_tree == own_tree:
                        l_score += 1
                        break
                    elif other_tree > own_tree:
                        break

                for other_tree in row[j+1:]:

                    if other_tree < own_tree:
                        r_score += 1
                    elif other_tree == own_tree:
                        r_score += 1
                        break
                    elif other_tree > own_tree:
                        break

                for other_tree in [row_[j] for row_ in grid][:i][::-1]:

                    if other_tree < own_tree:
                        u_score += 1
                    elif other_tree == own_tree:
                        u_score += 1
                        break
                    elif other_tree > own_tree:
                        break

                for other_tree in [row_[j] for row_ in grid][i+1:]:

                    if other_tree < own_tree:
                        d_score += 1
                    elif other_tree == own_tree:
                        d_score += 1
                        break
                    elif other_tree > own_tree:
                        break

                score = l_score * r_score * u_score * d_score
                if score > highscore:
                    highscore = score

        return highscore




if __name__ == '__main__':
    print('Solution to part one: ', solve(file_=file, part=1))
    print('Solution to part two: ', solve(file_=file, part=2))