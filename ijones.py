from collections import defaultdict
from typing import List


def find_ways_count(corridor: List, columns: int, rows: int):
    memorized_path = defaultdict(int)
    plates = [[1] for elem in range(rows)]

    for row in range(rows):
        memorized_path[corridor[row][0]] += 1

    for column in range(1, columns):
        all_ways = {}

        for row in range(rows):
            plate = corridor[row][column]

            if plate is not corridor[row][column - 1]:
                cur_way = plates[row][column - 1] + memorized_path[plate]
            else:
                cur_way = memorized_path[plate]

            plates[row].append(cur_way)
            all_ways[plate] = cur_way + all_ways.get(plate, 0)

        if column < columns:
            for plate in all_ways:
                memorized_path[plate] += all_ways[plate]

    if columns == 1:
        return plates[0][columns - 1]

    return plates[0][columns - 1] + plates[rows - 1][columns - 1]


if __name__ == '__main__':
    input_file = open("ijones.in", "r")
    row, column = map(int, input_file.readline().split())
    corridor = [[] for _ in range(row)]
    for plate in range(column):
        corridor[plate] = input_file.readline()
    input_file.close()

    output_file = open("ijones.out", "w")
    output_file.write(str(find_ways_count(corridor, row, column)))
