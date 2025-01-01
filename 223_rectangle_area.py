from itertools import combinations, product

def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    r1_x_vals, r1_y_vals = list(range(min(ax1, ax2), max(ax1, ax2))), list(range(min(ay1, ay2), max(ay1, ay2)))
    r2_x_vals, r2_y_vals = list(range(min(bx1, bx2), max(bx1, bx2))), list(range(min(by1, by2), max(by1, by2)))

    r1_pos = list(product(r1_x_vals, r1_y_vals))
    r2_pos = list(product(r2_x_vals, r2_y_vals))

    return len(set(r1_pos + r2_pos))

if __name__ == '__main__':
    print(computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))
