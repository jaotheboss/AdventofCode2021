with open("input.txt") as file:
    data = [i.strip() for i in file.readlines()]

char_dict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

illegal_char_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

legal_char_table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def scan_line(line: str) -> bool:
    order = []
    for char in line:
        if char in char_dict:
            order.append(char)
        else:
            start = order.pop()
            if char != char_dict[start]:
                return False, char, order
    return True, '', order


def tallying_illegal_points(data: list) -> int:
    point_total = 0
    for line in data:
        clear, illegal_char, _ = scan_line(line)
        if not clear:
            point_total += illegal_char_table[illegal_char]
    return point_total


print(tallying_illegal_points(data))


def filter_illegal_lines(data: list) -> list:
    return [line for line in data if scan_line(line)[0]]


def finish_sequence(last_order: list) -> list:
    completed_sequence = [char_dict[last_order[i]]
                          for i in range(len(last_order) - 1, -1, -1)]
    return ''.join(completed_sequence)


def tallying_autocomplete_score(data: list) -> int:
    autocomplete_scores = []
    for line in data:
        clear, _, last_order = scan_line(line)
        if clear:
            autocomplete_sequence = finish_sequence(last_order)
            current_score = 0
            for i in autocomplete_sequence:
                current_score *= 5
                current_score += legal_char_table[i]
            autocomplete_scores.append(current_score)
    return autocomplete_scores


def sorting_autocomplete_scores(scores: list) -> int:
    scores = sorted(scores)
    return scores[int((len(scores) - 1) / 2)]


def part_2(data: list) -> int:
    scores = tallying_autocomplete_score(data)
    return sorting_autocomplete_scores(scores)


print(part_2(data))
