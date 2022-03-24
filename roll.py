#!/usr/bin/env python3
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'dice', type=str, help='number and type of dice you want to roll with or without a modifier. ex: 2d20+4')

    return parser.parse_args()


def main():
    args = parse_args()
    print(f'ARG: {args.dice}')


if __name__ == "__main__":
    main()
