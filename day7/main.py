with open("input.txt") as file:
    data = [int(i) for i in file.readline().split(',')]


def mean(data: list) -> float:
    mean = sum(data) / len(data)
    return int(mean) + int(mean % 1 >= 0.5)


def mode(data: list) -> int:
    return max(data, key=data.count)


def calculate_fuel_use(start: int, end: int) -> int:
    return sum([i + 1 for i in range(abs(end - start))])


def calculate_total_fuel_use(data: list, value: int, part: int) -> int:
    if part == 1:
        return sum([abs(i - value) for i in data])
    elif part == 2:
        return sum([calculate_fuel_use(i, value) for i in data])


def check_neighboring_values(data: list, value: int, fuel_used: int) -> [bool, bool]:
    right = sum([calculate_fuel_use(i, value + 1) for i in data]) < fuel_used
    if value < 1:
        left = False
    else:
        left = sum([calculate_fuel_use(i, value - 1)
                   for i in data]) < fuel_used
    return left, right


def part_1(data: list) -> int:
    value, lowest_fuel_used = None, None
    for possible_anchor in set(data):
        fuel_used = calculate_total_fuel_use(data, possible_anchor, 1)
        if lowest_fuel_used == None or fuel_used < lowest_fuel_used:
            lowest_fuel_used = fuel_used
            value = possible_anchor
    return value, lowest_fuel_used


print(part_1(data))


def part_2(data: list) -> int:
    value = mean(data)
    lowest_fuel_used = calculate_total_fuel_use(data, value, 2)
    left_lower, right_lower = check_neighboring_values(
        data, value, lowest_fuel_used)
    while left_lower or right_lower:
        if left_lower:
            value -= 1
        elif right_lower:
            value += 1
        lowest_fuel_used = calculate_total_fuel_use(data, value, 2)
        left_lower, right_lower = check_neighboring_values(
            data, value, lowest_fuel_used)
    return value, lowest_fuel_used


print(part_2(data))
