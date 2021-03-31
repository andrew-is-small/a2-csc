"""
Really shitty code, written by github.com/dungwoong
Used to test random stuff
"""
from sudoku_puzzle import SudokuPuzzle
from solver import BfsSolver
from word_ladder_puzzle import WordLadderPuzzle

# sample usage of BfsSolver
def bfs_demo():
    a = BfsSolver()
    s = SudokuPuzzle(4,
                     [["A", "B", "C", "D"],
                      ["C", "D", " ", " "],
                      [" ", " ", " ", " "],
                      [" ", " ", " ", " "]], {"A", "B", "C", "D"})
    longst = a.solve(s)
    print("The puzzle was: ")
    print(s)
    print("The solution is: ")
    for i in longst:
        print(i)
        print("########")

def bfs_demo1():
    a = BfsSolver()
    b = WordLadderPuzzle("me", "my", {"me", "be", "my"})
    bongst = a.solve(b)
    print("The puzzle was: ")
    print(b)
    print("The solution is: ")
    for i in bongst:
        print(i)

bfs_demo1()


