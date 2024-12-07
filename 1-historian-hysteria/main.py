#!/usr/bin/env python

import part1, part2
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="Day 1 Solver",
        description="Historian Hysteria - Comparing Lists",
        epilog="Check the AOC Page for info on the challenge"
    )
    parser.add_argument("filename") # Input from AOC
    # Solve either Part 1 or Part 2
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-p1", "--part1", action="store_true")
    group.add_argument("-p2", "--part2", action="store_true")
    args = parser.parse_args();
    
    if args.part1:
        part1.run(args.filename)
    elif args.part2:
        part2.run(args.filename)

if __name__ == "__main__":
    main()