import logging
from typing import Any


def get_int_list_from_file(file_path: str) -> list[int]:
    int_list = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            try:
                int_list.append(int(line))
            except ValueError:
                logging.error(f'cant process line {line} and we will skip it')
    return int_list


def int_sum(int_list: list[int]):
    sum_amount = 0
    for number in int_list:
        sum_amount += number
    return sum_amount


def get_list_len(some_list: list[Any]):
    counter = 0
    for _ in some_list:
        counter += 1
    return counter


file_name_str = 'random_nums.txt'


if __name__ == '__main__':
    ints_list = get_int_list_from_file(file_name_str)
    numbers_sum = int_sum(ints_list)
    int_list_len = get_list_len(ints_list)

    print(f'total = {len(ints_list)}')
    print(f'summation = {numbers_sum}')
    print(f'average = {round(numbers_sum / int_list_len)}')
    print(f'Minimum = {min(ints_list)}')
    print(f'Maximum = {max(ints_list)}')

