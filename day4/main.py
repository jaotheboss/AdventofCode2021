from copy import deepcopy

with open("input.txt") as file:
    bingo_boards = []
    current_board = []
    for i, row in enumerate(file.readlines()):
        if i == 0:
            bingo_sequence = [int(i) for i in row.split(',')]
        else:
            if i % 6 == 1:
                if current_board:
                    bingo_boards.append(current_board)
                    current_board = []  # can't use current_board.clear()
                else:
                    continue
            else:
                current_board.append([int(value) for value in row.split()])


def rotate_board(bingo_board: list) -> list:
    return [[bingo_board[j][i] for j in range(5)] for i in range(5)]


def check_for_bingo(bingo_board: list) -> bool:
    for row in bingo_board:
        if row[0] != -1:
            continue
        elif all([i == -1 for i in row]):
            return True

    for col in rotate_board(bingo_board):
        if col[0] != -1:
            continue
        elif all([i == -1 for i in col]):
            return True
    return False


def check_off_number(bingo_board: list, number: int) -> list:
    return [[-1 if value == number else value for value in row] for row in bingo_board]


def calculate_unchecked_numbers(bingo_board: list) -> int:
    total_sum = 0
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] != -1:
                total_sum += bingo_board[i][j]
    return total_sum


def part_1(bingo_sequence: list, bingo_boards: list) -> int:
    updated_boards = [deepcopy(board) for board in bingo_boards]
    for number in bingo_sequence:
        updated_boards = [check_off_number(
            board, number) for board in updated_boards]
        for board in updated_boards:
            if check_for_bingo(board):
                return calculate_unchecked_numbers(board) * number


# print(part_1(bingo_sequence, bingo_boards))


def part_2(bingo_sequence: list, bingo_boards: list) -> int:
    updated_boards = [deepcopy(board) for board in bingo_boards]
    for number in bingo_sequence:
        updated_boards = [check_off_number(
            board, number) for board in updated_boards]
        for board in updated_boards:
            if check_for_bingo(board) and len(updated_boards) == 1:
                return calculate_unchecked_numbers(board) * number
            elif check_for_bingo(board):
                updated_boards.remove(board)


print(part_2(bingo_sequence, bingo_boards))
