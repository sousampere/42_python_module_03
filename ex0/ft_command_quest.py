#!/bin/bash/python3

import sys

print("=== Command Quest ===")
av = sys.argv
ac = len(av)
if (ac == 1):
    print("No arguments provided!")
    print(f"Program name: {av[0]}")
    print(f"Total arguments: {ac}")
else:
    print(f"Program name: {av[0]}")
    print(f"Arguments recieved: {ac - 1}")
    count = 0
    for arg in av:
        print(f"Argument {count}: {arg}")
        count += 1
    print(f"Total arguments: {ac}")
