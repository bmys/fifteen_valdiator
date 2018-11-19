import numpy as np
from validator import Game
from validator import load_solution
from validator import load_puzzle

# state_array = np.array(
# [
# [1, 2, 0,  3],
# [5, 6,  7, 4],
# [9, 10,11, 8],
# [13, 14, 15, 12 ]
# ])

# state_array = np.array(
# [
# [1, 2, 3,  4],
# [5, 6,  7, 8],
# [9, 10,11, 0],
# [13, 14, 15, 12]
# ])

# g = Game(state_array)
# g.solve('UUDDD')

print(load_solution('sol.txt'))