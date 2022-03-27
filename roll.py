#!/usr/bin/env python3
import argparse
from random import randint
import sys
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'dice', type=str, help='number and type of dice you want to roll with or without a modifier. ex: 2d20+4')

    return parser.parse_args()


def parse_roll_expression(roll_expression):
    '''
    Using regex we validate the given roll expression is valid and extract all the values we need from itt
    Extracted values are returned as a tuple
    Assuming nobody needs to roll more than 99 dice
    Allowing only existing D&D dice: d4, d6, d8, d10, d20, d100
    Regex breakdown:
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


def roll_dice(num_of_dice, die_type):
    num_of_dice_int = int(num_of_dice)
    die_type_int = int(die_type)
    print(f'🎲 Rolling {num_of_dice_int} d{die_type_int} 🎲')
    total = 0
    for i in range(num_of_dice_int):
        roll = randint(1, die_type_int)
        print(f'Die number {i+1} rolled {roll}')
        total += roll
    print(f'Total roll without modifier: {total}')
    return total


def modify_roll(roll_result, modifier_operator, roll_modifier):
    '''
    Adding or subtracting a modifier from a roll.
    Forsing values to int to bwe consistent 
    Allowing only '+' and '-' operators. Ignoring any other
    '''
    if (not modifier_operator) or (not roll_modifier):
        return roll_result
    roll_result_int = int(roll_result)
    roll_modifier_int = int(roll_modifier)
    result = roll_result_int
    if modifier_operator == '+':
        result += roll_modifier_int
    elif modifier_operator == '-':
        result -= roll_modifier_int
    return result


def main():
    args = parse_args()
    regex_groups = parse_roll_expression(args.dice)
    num_of_dice, die_type, modifier_operator, roll_modifier = regex_groups
    roll_result = roll_dice(num_of_dice, die_type)
    modified_roll = modify_roll(roll_result, modifier_operator, roll_modifier)
    print(f'Total roll with modifier: {modified_roll}')
    # check if i need pipenv
    # pretty output


if __name__ == "__main__":
    main()
