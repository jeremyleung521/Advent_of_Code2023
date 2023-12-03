# Day1.py
#
# First attempt at doing Day 1 of Advent of Code 2023

import time
import numpy
from collections import OrderedDict

map_words_dict = OrderedDict({'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                              "eight": '8', 'nine': '9', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
                              '7': '7', '8': '8', '9': '9'})


def read_input2(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    final_count = []
    for entry in read_list:
        temp_string = ''
        # Find first number
        blah = []
        for key, val in map_words_dict.items():
            pos = entry.find(key)
            if pos > -1:
                blah.append(pos)
            else:
                blah.append(200)

        print(blah)
        temp_string += list(map_words_dict.values())[numpy.argmin(blah)]

        # Find last number
        blah = []
        for key, val in map_words_dict.items():
            pos = entry[::-1].find(key[::-1])
            if pos > -1:
                blah.append(pos)
            else:
                blah.append(200)
        temp_string += list(map_words_dict.values())[numpy.argmin(blah)]

        #print(temp_string)
        final_count.append(int(temp_string))

    return sum(final_count)


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    final_count = []
    for entry in read_list:
        temp_string = ''

        for i in range(len(entry)):
            try:
                int(entry[i])
                temp_string += entry[i]
                break
            except ValueError:
                pass

        for i in range(len(entry) - 1, -1, -1):
            try:
                int(entry[i])
                temp_string += entry[i]
                break
            except ValueError:
                pass

        # print(temp_string)
        final_count.append(int(temp_string))

    return sum(final_count)


def main():
    ## Part 1
    # answer = read_input("Day1_test_input.txt")
    answer = read_input("Day1_input.txt")
    # answer = return_max(b)
    print(f'Sum is {answer}.')


def main2():
    # Part 2
    #answer2 = read_input2("Day1_test_input2.txt")
    answer2 = read_input2("Day1_input.txt")

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
