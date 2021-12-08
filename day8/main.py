with open("input.txt") as file:
    data = []
    for line in file.readlines():
        input, output = line.split("|")
        input = [i.strip() for i in input.split()]
        output = [i.strip() for i in output.split()]
        data.append({"input": input, "output": output})


def part_1(data: list) -> int:
    return sum([1 if len(code) in [2, 3, 4, 7] else 0 for line in data for code in line["output"]])


print(part_1(data))


def remove_letters(to_remove: str, from_string: str) -> str:
    for letter in to_remove:
        from_string = from_string.replace(letter, '')
    return from_string


def initial_decode(input: list) -> dict:
    signal_map = {}
    length_5, length_6 = [], []
    for signal in input:
        if len(signal) == 2:
            signal_map['1'] = signal
        elif len(signal) == 3:
            signal_map['7'] = signal
        elif len(signal) == 4:
            signal_map['4'] = signal
        elif len(signal) == 7:
            signal_map['8'] = signal
        elif len(signal) == 5:
            length_5.append(signal)
        elif len(signal) == 6:
            length_6.append(signal)
    return signal_map, length_5, length_6


def decode_length_5(line: list, signal_map: dict) -> dict:
    for signal in line:
        three_lines = remove_letters(signal_map['1'], signal)
        if len(three_lines) == 3:
            signal_map['3'] = signal
            break
    line = [i for i in line if i != signal]
    two_and_five = ''.join(line)
    two_and_five = remove_letters(three_lines, two_and_five)
    bottom_left = remove_letters(signal_map['4'], two_and_five)
    for signal in line:
        if bottom_left in signal:
            signal_map['2'] = signal
        else:
            signal_map['5'] = signal
    return signal_map, bottom_left


def decode_length_6(line: list, signal_map: dict, bottom_left: str) -> dict:
    for signal in line:
        if bottom_left not in signal:
            signal_map['9'] = signal
            break
    line = [i for i in line if i != signal]
    for signal in line:
        temp = remove_letters(bottom_left, signal)
        if set(temp) == set(signal_map['5']):
            signal_map['6'] = signal
        else:
            signal_map['0'] = signal
    return signal_map


def decode_signal_pattern(line: dict) -> dict:
    line = line['input']
    signal_map, length_5, length_6 = initial_decode(line)
    signal_map, bottom_left = decode_length_5(length_5, signal_map)
    signal_map = decode_length_6(length_6, signal_map, bottom_left)
    return signal_map


def decode_output(line: dict, signal_map: dict) -> int:
    line = [''.join(sorted(i)) for i in line['output']]
    inverted_map = {''.join(sorted(value)): key for key,
                    value in signal_map.items()}
    output_value = ''.join([inverted_map[i] for i in line])
    return eval(output_value.lstrip('0'))


def part_2(data: list) -> int:
    total_sum = 0
    for signal in data:
        signal_map = decode_signal_pattern(signal)
        output_value = decode_output(signal, signal_map)
        # print(signal['output'], output_value)
        total_sum += output_value
    return total_sum


print(part_2(data))
