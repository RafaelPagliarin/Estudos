from itertools import permutations

def check_row(I, x):
    if set(I) != {1, 2, 3, 4}:
        return False
    v, h = 1, I[0]
    for i in I[1:]:
        if i > h:
            h = i
            v += 1
    return v == x or x == 0

def check_grid(a, b, c, d, x, y):
    # a, b, c, d: 4 rows/ 4 columns
    # x, y: pair of clues
    for i in range(len(a)):
        col = [a[i], b[i], c[i], d[i]]
        if not check_row(col, x[i]) or not check_row(col[::-1], y[::-1][i]):
            return False
    return True

def gen_arr(a, b):
    # generate possible rows based on pair of clues
    L = [1, 2, 3, 4]
    return [o for o in permutations(L)
            if check_row(o, a) and check_row(o[::-1], b)]


def solve_puzzle(clues):
    rows = [gen_arr(clues[15 - i], clues[i + 4]) for i in range(0, 4)]
    return [tuple([a, b, c, d]) for a in rows[0] for b in rows[1] for c in rows[2] for d in rows[3] if
            check_grid(a, b, c, d, clues[:4], clues[8:12])][0]


print(solve_puzzle(( 0, 0, 1, 2,
              0, 2, 0, 0,
              0, 3, 0, 0,
              0, 1, 0, 0 )))


