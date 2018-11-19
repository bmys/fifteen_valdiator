import numpy as np
import operator
import sys

class Game:

    def __init__(self, arr):

        self.frame = arr
        self.zero_position = find_zero(self.frame)
        self.frame_size = tuple(map(operator.sub, self.frame.shape, (1, 1)))
        self.visited = set()
        # Create goal matrix
        self.goal_matrix = np.arange(1, self.frame.size+1).reshape(arr.shape)
        self.goal_matrix[-1][-1] = 0

        self.choose = {
            'L': (0, -1),
            'R': (0, 1),
            'U': (-1, 0),
            'D': (1, 0)
        }
        self.visited.add(hash(self.frame.tostring()))

    def available_moves(self, zero_position):

        moves = ['L', 'D', 'U', 'R']

        if zero_position[1] == 0:
            moves.remove('L')

        if zero_position[1] == self.frame_size[1]:
            moves.remove('R')

        if zero_position[0] == 0:
            moves.remove('U')

        if zero_position[0] == self.frame_size[0]:
            moves.remove('D')

        return moves

    def check_result(self):

        if np.array_equal(self.frame, self.goal_matrix):
            return True
        return False

    def move(self, direction):

        if direction not in self.available_moves(self.zero_position):
            return False

        new_place = tuple(map(operator.add, self.zero_position, self.choose[direction]))

        # swap elements
        self.frame[self.zero_position], self.frame[new_place] = \
            self.frame[new_place], self.frame[self.zero_position]

        self.zero_position = new_place

    def solve(self, path):
        loop = 0

        for move in path:
            if self.move(move) is False:
                print('\033[91mError: Bad move\033[0m')
                if loop > 0:
                    print(f'\033[93mWarning: loop detected {loop} times\033[0m')
                return

            if hash(self.frame.tostring()) in self.visited:
                loop += 1
            self.visited.add(hash(self.frame.tostring()))

        msg = '\033[92m✓ Correct\033[0m' if self.check_result() else '\033[91m❌ Incorrect\033[0m'
        print(msg)
        if loop > 0:
            print(f'\033[93m⚠ Warning: loop detected {loop} times\033[0m')


def find_zero(frame):
    temp = np.where(frame == 0)
    temp = tuple(np.concatenate(temp, axis=0))
    return temp


def load_puzzle(file_name):
    with open(file_name, 'r') as file:
        text = file.read().splitlines()
    text = text[1:]

    for idx, line in enumerate(text):
        text[idx] = tuple(int(i) for i in line.split(' '))
    return np.array(text)


def load_solution(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    return text


# if __name__ == 'validator':
#     assert len(sys.argv) is 3
#
#     puzzle = load_puzzle(sys.argv[1])
#     solution = load_solution(sys.argv[2])
#     solver = Game(puzzle)
#     solver.solve(solution)