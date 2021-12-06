with open("input.txt") as file:
    data = {i: 0 for i in range(9)}
    for i in file.readlines()[0].split(','):
        data[int(i)] += 1


def pass_one_day(data: dict) -> int:
    new_fish = data[0]
    for i in range(8):
        data[i] = data[i + 1]
    data[6] += new_fish
    data[8] = new_fish


for day in range(256):
    pass_one_day(data)
    if day == 79:
        print("Part 1: {}".format(sum(data.values())))
    if day == 255:
        print("Part 2: {}".format(sum(data.values())))
