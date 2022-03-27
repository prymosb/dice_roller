#!/usr/bin/env python3
import argparse
import sys
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'dice', type=str, help='number and type of dice you want to roll with or without a modifier. ex: 2d20+4')

    return parser.parse_args()


def parse_roll_expression(roll_expression):
    '''
    Assuming nobody needs to roll more than 99 dice
    Allowing only existing D&D dice: d4, d6, d8, d10, d20, d100
    ^ - beginning of the expression
    ([1-9]|[1-9][0-9]) - one or two digits where the first one is not zero
    d - letter 'd'
    (4|6|8|10|20|100) - digit 4 or 6 or 8 etc
    (?:\+([1-9]|[1-9][0-9]))? - expression responsible for the modifier of the roll
        (?:<something here>)? - this part makes the section optional. use may or may not specify the modifier
        \+ - literal plus sign
        ([1-9]|[1-9][0-9]) - one or two digits where the first one is not zero
    $ - end of the expression
    '''
    regex = r'^([1-9]|[1-9][0-9])d(4|6|8|10|20|100)(?:(\+|\-)([1-9]|[1-9][0-9]))?$'
    roll_expression_regex = re.compile(regex)
    regex_result = roll_expression_regex.search(roll_expression)
    regex_groups = ''
    try:
        regex_groups = regex_result.groups()
    except AttributeError as e:
        print(f'Provided expression {roll_expression} is not valid')
        sys.exit()

    return regex_groups


def main():
    args = parse_args()
    regex_groups = parse_roll_expression(args.dice)
    num_of_dice, die_type, modifier_operator, roll_modifier = regex_groups
    # check regex matches
    # split string
    # figure out the die
    # roll
    # add modifier
    # pretty output
    print(f'ROLL EXPRESSION: {args.dice}')
    print(
        f'num_of_dice={num_of_dice}, die_type={die_type}, modifier_operator={modifier_operator}, roll_modifier={roll_modifier}')


if __name__ == "__main__":
    main()
