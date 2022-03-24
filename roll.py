#!/usr/bin/env python3
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('roll', type=str)

    return parser.parse_args()


def main():
    args = parse_args()
    print(f'ARG: {args.roll}')


if __name__ == "__main__":
    main()
