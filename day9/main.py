with open("input.txt") as file:
    data = []
    for row in file.readlines():
        data.append([int(i) for i in row.strip()])


def check_left(i: int, j: int, h_map: list) -> bool:
    if i == 0:
        return True
    else:
        return h_map[j][i] < h_map[j][i - 1]


def check_right(i: int, j: int, h_map: list) -> bool:
    if i == len(h_map[0]) - 1:
        return True
    else:
        return h_map[j][i] < h_map[j][i + 1]


def check_up(i: int, j: int, h_map: list) -> bool:
    if j == 0:
        return True
    else:
        return h_map[j][i] < h_map[j - 1][i]


def check_down(i: int, j: int, h_map: list) -> bool:
    if j == len(h_map) - 1:
        return True
    else:
        return h_map[j][i] < h_map[j + 1][i]


def find_low_points(data: list) -> dict:
    low_point = {}
    for j in range(len(data)):
        for i in range(len(data[0])):
            if check_left(i, j, data) and check_right(i, j, data) and check_up(i, j, data) and check_down(i, j, data):
                low_point[(i, j)] = data[j][i]
    return low_point


def find_risk_level(data: list) -> int:
    low_points = find_low_points(data)
    return sum([i + 1 for i in low_points.values()])


print(find_risk_level(data))


def get_valid_neighbours(i: int, j: int, n_row: int, n_col: int) -> list:
    up, down = (i, j - 1), (i, j + 1)
    left, right = (i - 1, j), (i + 1, j)
    valid_sides = []
    if i > 0:
        valid_sides.append(left)
    if i < n_col - 1:
        valid_sides.append(right)
    if j > 0:
        valid_sides.append(up)
    if j < n_row - 1:
        valid_sides.append(down)
    return valid_sides


def traverse_surrounding(data: list, position: tuple) -> int:
    n_row, n_col = len(data), len(data[0])
    visited = {(i, j): False for i in range(
        len(data[0])) for j in range(len(data))}
    to_visit = [position]

    while to_visit:
        current_spot = to_visit.pop(0)  # FIFO; BFS
        visited[tuple(current_spot)] = True
        i, j = current_spot
        valid_sides = get_valid_neighbours(i, j, n_row, n_col)
        for x, y in valid_sides:
            if not visited[(x, y)] and data[y][x] != 9:  # data[y][x] - data[j][i] == 1 and
                to_visit.append((x, y))
                visited[(x, y)] = True
    return sum(visited.values())


def get_basin_sizes(data: list) -> list:
    low_points = find_low_points(data)
    basin_sizes = [traverse_surrounding(
        data, coordinate) for coordinate in low_points]
    return sorted(basin_sizes)


def part_2(data: list) -> int:
    basin_sizes = get_basin_sizes(data)
    total_sum = 1
    for i in basin_sizes[-3:]:
        total_sum *= i
    return total_sum


print(part_2(data))
