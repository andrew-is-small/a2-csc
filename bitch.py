"""
Really shitty code, written by github.com/dungwoong
Used to test random stuff
"""
from sudoku_puzzle import SudokuPuzzle
from solver import BfsSolver, DfsSolver
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


def wl_bfs_demo1():
    a = BfsSolver()
    b = WordLadderPuzzle("me", "my", {"me", "be", "my"})
    bongst = a.solve(b)
    print("The puzzle was: ")
    print(b)
    print("The solution is: ")
    for i in bongst:
        print(i)


def wl_bfs_demo2():
    a = BfsSolver()
    b = WordLadderPuzzle("cost", "save",
                         {"cost", "cast", "case", "cave", "save", "cyst"})
    # cost cast case cave save btw
    bongst = a.solve(b)
    print("The puzzle was: ")
    print(b)
    print("The solution is: ")
    for i in bongst:
        print(i)


def wl_dfs_demo():
    a = DfsSolver()
    b = WordLadderPuzzle("cost", "save",
                         {"cost", "cyst", "cest",
                          "case", "cave", "save", "cast"})
    # cost cast case cave save btw
    bongst = a.solve(b)
    print("The puzzle was: ")
    print(b)
    print("The solution is: ")
    for i in bongst:
        print(i)


def wl_bfs_demo_repeats():
    a = BfsSolver()
    b = WordLadderPuzzle("cost", "save",
                         {"cost", "cyst", "cest", "cist", "cxst", "clst",
                          "case", "cave", "sive", "sove", "save", "cast"})
    bongst = a.solve(b)
    print("The puzzle was: ")
    print(b)
    print("The solution is: ")
    for i in bongst:
        print(i)


def wl_get_diff():
    b = WordLadderPuzzle("cost", "savi",
                         {"cost", "cyst", "cest", "cist", "cxst", "savi",
                          "case", "cave", "sive", "sove", "save", "cast"})
    a = BfsSolver()
    bongst = a.solve(b)
    print("The puzzle was: ")
    print(b)
    print("The solution is: ")
    for i in bongst:
        print(i)
    print(b.get_difficulty())


wl_get_diff()
# TODO BFS DOESN'T GIVE SHORTEST SOLUTION??
# TODO DFS DOESN'T EITHER LOL OH WAIT ITS ALBERTS FAULT AHHHHH
# implement the checker method which basically takes every gamestate in a
# solution and checks if the next gamestates are already in its extensions
# and removes them if it is.
# REMEMBER TO DELETE FROM THE BACK
# REMEMBER TO SEARCH EVERY FUTURE GAMESTATE AND STOP SEARCHING ONLY IF
# YOU CANT REACH IN EXTENSIONS ANYMORE
# no just don't add to gamestate if nongism
