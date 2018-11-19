#!/usr/bin/python3

from sys import argv
from validator import *

if len(argv) > 1:
    puzzle, solution = argv[1], argv[2]

    puzzle = load_puzzle('puzzles/' + puzzle)
    solution = load_solution('solutions/' + solution)

    solver = Game(puzzle)
    solver.solve(solution)


