with open("input.txt") as file:
    data = []
    for row in file.readlines():
        start, end = row.split("->")
        data.append([[int(i) for i in start.split(',')], [int(i)
                    for i in end.split(',')]])


def update_mapped_path(mapped_path: dict, coordinate: list) -> dict:
    if coordinate not in mapped_path:
        mapped_path[coordinate] = 1
    else:
        mapped_path[coordinate] += 1
    return mapped_path


def draw_path(point_a: list, point_b: list, mapped_path: dict, diagonal: bool = False) -> dict:
    if point_a[0] == point_b[0] or point_a[1] == point_b[1]:
        if point_a[0] <= point_b[0]:
            start_x, end_x = point_a[0], point_b[0] + 1
        else:
            start_x, end_x = point_b[0], point_a[0] + 1

        if point_a[1] <= point_b[1]:
            start_y, end_y = point_a[1], point_b[1] + 1
        else:
            start_y, end_y = point_b[1], point_a[1] + 1

        for x_coordinate in range(start_x, end_x):
            for y_coordinate in range(start_y, end_y):
                mapped_path = update_mapped_path(
                    mapped_path, (x_coordinate, y_coordinate))
        return mapped_path
    elif diagonal:
        start, end = sorted([point_a, point_b])
        if end[1] > start[1]:
            incline = True
        else:
            incline = False

        y_coordinate = start[1]
        for x_coordinate in range(start[0], end[0] + 1):
            mapped_path = update_mapped_path(
                mapped_path, (x_coordinate, y_coordinate))
            if incline:
                y_coordinate += 1
            else:
                y_coordinate -= 1
        return mapped_path
    else:
        return mapped_path


def part_1(data: list) -> int:
    resulting_path = {}
    for coordinate in data:
        resulting_path = draw_path(
            coordinate[0], coordinate[1], resulting_path)
    return sum([i >= 2 for i in resulting_path.values()])


print(part_1(data))


def part_2(data: list) -> int:
    resulting_path = {}
    for coordinate in data:
        resulting_path = draw_path(
            coordinate[0], coordinate[1], resulting_path, True)
    return sum([i >= 2 for i in resulting_path.values()])


print(part_2(data))
