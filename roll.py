#!/usr/bin/env python3
import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'dice', type=str, help='number and type of dice you want to roll with or without a modifier. ex: 2d20+4')

    return parser.parse_args()


def is_valid_roll(roll_expression):
    # Assuming nobody needs to roll more than 99 dice
    # Allowing only existing D&D dice: d4, d6, d8, d10, d20, d100
    # ^ - beginning of the expression
    # ([1-9]|[1-9][0-9]) - one or two digits where the first one is not zero
    # d - letter 'd'
    # (4|6|8|10|20|100) - digit 4 or 6 or 8 etc
    # \+ - plus sign
    # ([1-9]|[1-9][0-9]) - one or two digits where the first one is not zero
    # $ - end of the expression
    # (4|6|8|10|20|100)\+([1-9]{1,2})$'
    regex = r'^([1-9]|[1-9][0-9])d(4|6|8|10|20|100)(?:(\+[1-9]|\+[1-9][0-9]))$'
    roll_expression_regex = re.compile(regex)
    regex_result = roll_expression_regex.search(roll_expression)
    regex_result.group()
    g1 = regex_result.group(1)
    g2 = regex_result.group(2)
    g3 = regex_result.group(3)
    print(f'roll {g1} of d{g2} dice and {g3}')
    return True


def main():
    args = parse_args()
    if not is_valid_roll(args.dice):
        raise Exception('Roll expression is not valid')
    # check regex matches
    # split string
    # figure out the die
    # roll
    # add modifier
    # pretty output
    print(f'ARG: {args.dice}')


if __name__ == "__main__":
    main()
