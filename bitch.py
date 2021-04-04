"""
Really shitty code, written by github.com/dungwoong
Used to test random stuff
"""
from sudoku_puzzle import SudokuPuzzle
from solver import BfsSolver, DfsSolver
from word_ladder_puzzle import WordLadderPuzzle
from expression_tree_puzzle import ExpressionTreePuzzle
from expression_tree import ExprTree


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


def mutate_test_exp_tree():
    exp_t2 = ExprTree('+', [ExprTree('a', []), ExprTree(1, [])])
    puz2 = ExpressionTreePuzzle(exp_t2, 8)
    exts_of_puz2 = puz2.extensions()
    print(puz2)
    print(exts_of_puz2[0])
    print("########")
    exts_of_puz2[0]._tree.substitute({'a': 69})
    exts_of_puz2[0].variables['a'] = 69
    # LOL I LOVE HOW ITS LIKE pwease don't access a pwivate variable uwu
    print(exts_of_puz2[0])
    print(puz2)
    # ok I think the .copy method worked? not sure tho


def exp_tree_puzzle_both_solvers():
    exp_t = ExprTree('+', [ExprTree('a', []), ExprTree('b', [])])
    nong_t = ExprTree('*', [exp_t, ExprTree(3, [])])
    puz = ExpressionTreePuzzle(nong_t, 33)
    print(puz.fail_fast())
    dfs = DfsSolver()
    bongst = dfs.solve(puz)
    print("The puzzle was: ")
    print(puz)
    print("The solution is: ")
    for i in bongst:
        print(i)


def exp_tree_not_solvable():
    exp_t = ExprTree('*', [ExprTree('a', []), ExprTree(3, [])])
    puz = ExpressionTreePuzzle(exp_t, 5)
    dfs = BfsSolver()
    bongst = dfs.solve(puz)
    print("The puzzle was: ")
    print(puz)
    print("The solution is: ")
    for i in bongst:
        print(i)


def exp_tree_ex():
    puz = WordLadderPuzzle("done", "done", {"done"})
    print(puz.get_difficulty())


def wl_extensions():
    b = WordLadderPuzzle("cost", "case",
                         {"cost", "cast", "yost", "cose",
                          "case", "cyst", "colt"})
    # yost doesn't get you closer
    # cast gets u 1 closer
    # cose gets u 1 closer
    # cyst doesn't get you any closer
    # colt gets you further
    # so it should go (cast/cose), (cyst/yost), colt
    for i in b.extensions():
        print(i)


def wl_extensions_update_dfs_demo():
    puz = WordLadderPuzzle("same", "cost")
    dfs = DfsSolver()
    bongst = dfs.solve(puz)
    print("The puzzle was: ")
    print(puz)
    print("The solution is: ")
    for i in bongst:
        print(i)


wl_extensions_update_dfs_demo()
# TODO BFS DOESN'T GIVE SHORTEST SOLUTION??
# TODO DFS DOESN'T EITHER LOL OH WAIT ITS ALBERTS FAULT AHHHHH
# implement the checker method which basically takes every gamestate in a
# solution and checks if the next gamestates are already in its extensions
# and removes them if it is.
# REMEMBER TO DELETE FROM THE BACK
# REMEMBER TO SEARCH EVERY FUTURE GAMESTATE AND STOP SEARCHING ONLY IF
# YOU CANT REACH IN EXTENSIONS ANYMORE
# no just don't add to gamestate if nongism
