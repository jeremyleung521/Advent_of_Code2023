# Day2.py
#
# First attempt at doing Day 2 of Advent of Code 2022

import time
import numpy


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    return read_list


def return_sum(input_list):
    games_ok = []
    for entry in input_list:
        set_of_balls = {'red': 0, 'blue': 0, 'green': 0}
        [first_split, second_split] = entry.split(':',1)

        for each_round in second_split.split(';'):
            for color in each_round.split(', '):
                # print(color)
                [num, col] = color.rsplit(' ', 1)
                num = int(num)
                if num > set_of_balls[col]:
                    set_of_balls[col] = num

        if set_of_balls['red'] <= 12 and set_of_balls['green'] <= 13 and set_of_balls['blue'] <= 14:
            games_ok.append(int(first_split.split(' ')[1]))

    final_count = numpy.sum(games_ok)

    return final_count


def return_power(input_list):
    games_ok = []
    for entry in input_list:
        set_of_balls = {'red': 0, 'blue': 0, 'green': 0}
        [_, second_split] = entry.split(':', 1)

        for each_round in second_split.split(';'):
            for color in each_round.split(', '):
                # print(color)
                [num, col] = color.rsplit(' ', 1)
                num = int(num)
                if num > set_of_balls[col]:
                    set_of_balls[col] = num

        #print(list(set_of_balls.values()))
        games_ok.append(numpy.prod(list(set_of_balls.values())))

    #print(games_ok)
    final_count = numpy.sum(games_ok)

    return final_count

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
    #b = read_input("Day2_test_input.txt")
    b = read_input("Day2_input.txt")
    answer = return_sum(b)
    print(f'The sum is {answer}.')


def main2():
    # Part 2
    #a = read_input("Day2_test_input.txt")
    a = read_input("Day2_input.txt")
    answer2 = return_power(a)
    print(f'The sum is {answer2}.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
