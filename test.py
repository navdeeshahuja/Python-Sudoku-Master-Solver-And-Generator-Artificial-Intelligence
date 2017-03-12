
import SudokuMaster
board = SudokuMaster.makeBoard()
puzzle = SudokuMaster.makePuzzleBoard(board, "moderate")
SudokuMaster.printBoard(puzzle)
if SudokuMaster.solveBoard(puzzle):
    print("\n\n\nSolved Solution is: ")
    SudokuMaster.printBoard(puzzle)
else:
    print("No Solution Exist")
