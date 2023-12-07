# Day6.py
#
# First attempt at doing Day 6 of Advent of Code 2023

import time
import numpy


def read_input(file_name, n):
    input_array = numpy.loadtxt(file_name, usecols=tuple(range(1, n+1)), dtype=int)

    return input_array.T


def read_alt(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    return [int(line.split(':')[1].replace(' ', '')) for line in lines]


def calc_ways(given_time, dist):
    count = 0
    for i in range(1, given_time):
        predicted_dist = (given_time - i) * i  # Time left * time pressed
        if predicted_dist > dist:
            count += 1

    return count


def return_max(input_list):
    max_cal = numpy.max(input_list)
    where = numpy.where(input_list == max_cal)[0][0]

    return [int(max_cal), where]


def return_top3(input_list):
    sorted_list = sorted(input_list, key=lambda x: -x)
    cal_sum = sum(sorted_list[0:3])
    where_three = numpy.where(input_list > sorted_list[3])[0]

    return [int(cal_sum), where_three]


def main():
    ## Part 1
    #b = read_input("Day6_test_input.txt", 3)
    b = read_input("Day6_input.txt", 4)
    blah = []
    for x in b:
        blah.append(calc_ways(x[0], x[1]))
    answer = numpy.prod(blah)
    print(f'Answer is {answer}')


def main2():
    # Part 2
    # a = read_alt("Day6_test_input.txt")
    a = read_alt("Day6_input.txt")
    answer2 = calc_ways(a[0], a[1])
    print(f'Answer is {answer2}')


if __name__ == "__main__":
    ## Part 1
    #startTime = time.perf_counter()
    #main()
    #print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
