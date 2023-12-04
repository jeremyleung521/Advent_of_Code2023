# Day4.py
#
# First attempt at doing Day 4 of Advent of Code 2023

import time
import numpy


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    winning_nums, scratch_nums = [], []
    for entry in read_list:
        [winning, current] = entry.split(': ')[1].split(' | ')
        winning = [int(i) for i in winning.split(' ') if i != '']
        current = [int(i) for i in current.split(' ') if i != '']

        winning_nums.append(winning)
        scratch_nums.append(current)

    return winning_nums, scratch_nums


def process_scratch_cards(scratch_numbers, winning_numbers):
    count = 0
    for i in scratch_numbers:
        if i in winning_numbers:
            count += 1

    if count > 0:
        return 2 ** (count - 1)
    else:
        return 0


def duplicate_scratch(scratch_numbers, winning_numbers):
    count = 0
    for i in scratch_numbers:
        if i in winning_numbers:
            count += 1

    return count


def main():
    ## Part 1
    # winning, scratch = read_input("Day4_test_input.txt")
    winning, scratch = read_input("Day4_input.txt")

    answer = 0
    for i_winning, i_scratch in zip(winning, scratch):
        answer += process_scratch_cards(i_scratch, i_winning)

    print(f'Sum is {answer}.')


def main2():
    # Part 2
    #winning, scratch = read_input("Day4_test_input.txt")
    winning, scratch = read_input("Day4_input.txt")

    n_cards = [1 for i in range(len(scratch))]

    for x, (i, i_win, i_scratch) in enumerate(zip(n_cards, winning, scratch)):
        # print(x, i, i_win, i_scratch)
        n = duplicate_scratch(i_scratch, i_win)
        # print(n)
        for j in range(x+1, x+n+1):
            n_cards[j] += i

        # print(n_cards)

    # print(n_cards)
    answer2 = numpy.sum(n_cards)

    print(f'Sum is {answer2}.')

if __name__ == "__main__":
    ## Part 1
    # startTime = time.perf_counter()
    # main()
    # print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
