import numpy
from Sudoku import Sudoku


sudo = Sudoku()


# sudo.grid = numpy.array([[2, 5, 6, 8, 3, 0, 9, 0, 1],
#                          [0, 1, 0, 0, 0, 4, 0, 0, 0],
#                          [4, 0, 7, 0, 0, 0, 2, 0, 8],
#                          [0, 0, 5, 2, 0, 0, 0, 0, 0],
#                          [0, 0, 0, 0, 9, 8, 1, 0, 0],
#                          [0, 4, 0, 0, 0, 3, 0, 0, 0],
#                          [0, 0, 0, 3, 6, 0, 0, 7, 2],
#                          [0, 7, 0, 0, 0, 0, 0, 0, 3],
#                          [9, 0, 3, 0, 0, 0, 6, 0, 4]])




# sudo.grid = numpy.array([
#     [5, 0, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 9, 0, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [0, 0, 0, 8, 0, 0, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 0, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 0, 9]
# ])



# sudo.grid =  numpy.zeros(shape=(9,9))
# print(sudo.grid)

import time
start_time = time.time()
# sudo.createSudokuResolved(0)
# sudo.checkGrid()
sudo.solver()
print(sudo.grid)
# print("--------------------------------")
# sudo.solver()
# print(sudo.grid)
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)
