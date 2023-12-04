# Day3.py
#
# First attempt at doing Day 3 of Advent of Code 2023

import time
import numpy

numbers = [str(i) for i in range(0,10)]
symbols = ['*', '/','+', '-', '=', '$', '@', '#', '%', '&']


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    part_numbers = []
    number_pos = []
    symbol_pos = []
    for (row_pos, entry) in enumerate(read_list):
        temp_pos = []
        temp_row = []
        # making lists of all number positions and symbol positions
        for (num_x, letter) in enumerate(entry):
            if letter in numbers:  # If a number, add position to
                temp_pos.append([row_pos, num_x])
            else:
                if temp_pos:
                    temp_row.append(temp_pos)
                    temp_pos = []
                elif letter != '.':  # Probably a symbol
                    symbol_pos.append([row_pos, num_x])

        if temp_pos:
            temp_row.append(temp_pos)

        number_pos.append(temp_row)

        row = []
        # A list of all part numbers
        for replacement in symbols:
            entry = entry.replace(replacement, '.')

        for j in entry.split('.'):
            if j != '':
                try:
                    j = int(j)
                    row.append(j)
                except ValueError:
                    pass
        part_numbers.append(row)

    # print(part_numbers)
    # print(number_pos)
    # print(symbol_pos)

    return part_numbers, number_pos, symbol_pos


def read_input2(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    part_numbers = []
    number_pos = []
    symbol_pos = []
    asterisk_pos = []
    for (row_pos, entry) in enumerate(read_list):
        temp_pos = []
        temp_row = []
        # making lists of all number positions and symbol positions
        for (num_x, letter) in enumerate(entry):
            if letter in numbers:  # If a number, add position to
                temp_pos.append([row_pos, num_x])
            else:
                if temp_pos:
                    temp_row.append(temp_pos)
                    temp_pos = []
                if letter == '*':
                    asterisk_pos.append([row_pos, num_x])
                elif letter != '.':  # Probably a symbol
                    symbol_pos.append([row_pos, num_x])

        if temp_pos:
            temp_row.append(temp_pos)

        number_pos.append(temp_row)

        row = []
        # A list of all part numbers
        for replacement in symbols:
            entry = entry.replace(replacement, '.')

        for j in entry.split('.'):
            if j != '':
                try:
                    j = int(j)
                    row.append(j)
                except ValueError:
                    pass
        part_numbers.append(row)

    # print(part_numbers)
    # print(number_pos)
    # print(symbol_pos)

    return part_numbers, number_pos, symbol_pos, asterisk_pos

def check_neighbours(number_pos, symbol_pos):
    # print(number_pos)
    x, y = number_pos[0], number_pos[1]
    check = [[x+1, y], [x-1, y], [x, y+1], [x, y-1], [x+1, y+1], [x-1, y-1], [x+1, y-1], [x-1, y+1]]

    for check_coord in check:
        if check_coord in symbol_pos:
            #print(check_coord)
            return True

    return False


def main():
    ## Part 1
    # parts_numbers, number_pos, symbol_pos = read_input("Day3_test_input.txt")
    parts_numbers, number_pos, symbol_pos = read_input("Day3_input.txt")
    answer = 0
    for part_row, pos_row in zip(parts_numbers, number_pos):
        for part, pos in zip(part_row, pos_row):
            #print(part)
            for pos_coord in pos:
                if check_neighbours(pos_coord, symbol_pos):
                    answer += part
                    #print(part)
                    break
    print(f'Sum is {answer}.')


def main2():
    # Part 2
    # parts_numbers, number_pos, symbol_pos, asterisk_pos = read_input2("Day3_test_input.txt")
    parts_numbers, number_pos, symbol_pos, asterisk_pos = read_input2("Day3_input.txt")

    neighbours = [[] for i in range(len(asterisk_pos))]
    for idx, asterisk in enumerate(asterisk_pos):
        row = asterisk[0]
        for part_row, pos_row in zip(parts_numbers[row-1:row+2], number_pos[row-1:row+2]):
            for part, pos in zip(part_row, pos_row):
                for pos_coord in pos:
                    if check_neighbours(pos_coord, [asterisk]):
                        neighbours[idx].append(part)
                        break

    # print(neighbours)

    answer2 = 0
    for blah in neighbours:
        if len(blah) == 2:
            answer2 += numpy.prod(blah)
        else:
            if len(blah) < 2:
                pass
            else:
                raise ValueError(f'{blah} has a length ')
    print(f'Sum is {answer2}.')


if __name__ == "__main__":
    ## Part 1
    #startTime = time.perf_counter()
    #main()
    #print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
