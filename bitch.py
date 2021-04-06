"""
Really shitty code, written by github.com/dungwoong
Used to test random stuff
"""
from sudoku_puzzle import SudokuPuzzle
from word_ladder_puzzle import WordLadderPuzzle, MEDIUM
from expression_tree_puzzle import ExpressionTreePuzzle
from expression_tree import ExprTree
from sudoku_puzzle import SudokuPuzzle
from word_ladder_puzzle import WordLadderPuzzle, EASY, TRIVIAL, MEDIUM, IMPOSSIBLE, HARD
from solver import BfsSolver, DfsSolver


# sample usage of BfsSolver
def test_word_ladder_get_difficulty_extrawords() -> None:
    wl1 = WordLadderPuzzle("cost", "save", {"cost", "cast", "case",
                                            "cave", "rave", "have", "save"})
    assert wl1.get_difficulty() == MEDIUM


def test_word_ladder_get_difficulty_extrawords1() -> None:
    wl1 = WordLadderPuzzle("cost", "cast", {"cost", "cast"})
    assert wl1.get_difficulty() == TRIVIAL


def test_word_ladder_get_difficulty_extrawords2() -> None:
    wl1 = WordLadderPuzzle("cost", "case", {"cost", "cast", "case"})
    assert wl1.get_difficulty() == EASY


def test_word_ladder_get_difficulty_extrawords3() -> None:
    wl1 = WordLadderPuzzle("cost", "yo", {"cost", "cast", "case"})
    assert wl1.get_difficulty() == IMPOSSIBLE


def test_word_ladder_get_difficulty_extrawords4() -> None:
    wl1 = WordLadderPuzzle("cost", "sabe", {"cost", "cast", "case",
                                            "cave", "save", "sabe"})
    assert wl1.get_difficulty() == HARD


def test_word_ladder_eq_diff_order() -> None:
    wl1 = WordLadderPuzzle("cost", "save", {"cost", "cast", "case",
                                            "cave", "rave", "have", "save"})
    wl2 = WordLadderPuzzle("cost", "save", {"cost", "cast", "case",
                                            "cave", "rave", "have", "save"})
    wl3 = WordLadderPuzzle("mass", "save", {"cost", "cast", "case",
                                            "cave", "rave", "have", "save"})
    wl4 = WordLadderPuzzle("cost", "save", {"save", "rave", "cave",
                                            "case", "cast", "have", "cost"})
    assert wl1.__eq__(wl2) is True
    assert wl1.__eq__(wl3) is False
    assert wl1.__eq__(wl4) is True


def test_word_ladder_emptyset() -> None:
    wl1 = WordLadderPuzzle("cost", "save", {})
    wl2 = WordLadderPuzzle("cost", "save", {})
    wl3 = WordLadderPuzzle("mass", "save", {})
    assert wl1.__eq__(wl2) is True
    assert wl1.__eq__(wl3) is False


def test_word_ladder_eq_isolved() -> None:
    wl1 = WordLadderPuzzle("cost", "save", {"cost", "cast", "case",
                                            "cave", "rave", "have", "save"})
    wl2 = WordLadderPuzzle("save", "save", {"cost", "cast", "case",
                                            "cave", "rave", "have", "save"})
    assert wl1.is_solved() is False
    assert wl2.is_solved() is True


def test_word_ladder_eq_isolved_empty() -> None:
    wl1 = WordLadderPuzzle("", "", {"cost", "cast", "case",
                                            "cave", "rave", "have", "save"})
    assert wl1.is_solved() is True


def test_sudoku_eq1() -> None:
    r1 = ["A", "B", "C", "D"]
    r2 = ["D", "C", "B", "A"]
    r3 = [" ", "D", " ", " "]
    r4 = [" ", " ", " ", " "]
    s1 = SudokuPuzzle(4, [r1, r2, r3, r4], {"A", "B", "C", "D"})
    r1_2 = ["A", "B", "C", "D"]
    r2_2 = ["D", "C", "B", "A"]
    r3_2 = [" ", "D", " ", " "]
    r4_2 = [" ", " ", " ", " "]
    s2 = SudokuPuzzle(4, [r1_2, r2_2, r3_2, r4_2], {"A", "B", "C", "D"})
    assert s1 == s2


def test_sudoku_empty() -> None:
    r1 = [" ", " ", " ", " "]
    r2 = [" ", " ", " ", " "]
    r3 = [" ", " ", " ", " "]
    r4 = [" ", " ", " ", " "]
    s1 = SudokuPuzzle(4, [r1, r2, r3, r4], {})
    r1_2 = [" ", " ", " ", " "]
    r2_2 = [" ", " ", " ", " "]
    r3_2 = [" ", " ", " ", " "]
    r4_2 = [" ", " ", " ", " "]
    s2 = SudokuPuzzle(4, [r1_2, r2_2, r3_2, r4_2], {})
    assert s1 == s2


def test_sudoku_isolveed_true() -> None:
    r1 = ["A", "B", "C", "D"]
    r2 = ["C", "D", "A", "B"]
    r3 = ["B", "A", "D", "C"]
    r4 = ["D", "C", "B", "A"]
    grid = [r1, r2, r3, r4]
    s = SudokuPuzzle(4, grid, {"A", "B", "C", "D"})
    assert s.is_solved() is True


def test_sudoku_isolveed_false() -> None:
    r1 = ["A", "B", "C", "D"]
    r2 = ["C", "D", "A", "B"]
    r3 = ["B", "D", "A", "C"]  # "D" and "A" in this row are not valid.
    r4 = ["D", "C", "B", "A"]
    grid = [r1, r2, r3, r4]
    s = SudokuPuzzle(4, grid, {"A", "B", "C", "D"})
    assert s.is_solved() is False


def test_sudoku_failure_fast_true() -> None:
    s = SudokuPuzzle(4, \
                         [[" ", "A", "C", "B"], \
                          [" ", "B", "A", "D"], \
                          [" ", " ", "B", "A"], \
                          [" ", " ", "D", "C"]], {"A", "B", "C", "D"})
    y = SudokuPuzzle(4, [["B", "D", "A", "C"],
                         ["C", "A", "B", "D"],
                         ["A", "B", " ", " "],
                         [" ", " ", " ", " "]],
                     {"A", "B", "C", "D"})
    assert y.fail_fast() is True
    assert s.fail_fast() is True


def test_sudoku_failure_fast_false() -> None:
    s = SudokuPuzzle(4, [["C", "D", "B", "A"],
                         ["B", "A", "D", "C"],
                         ["D", "C", "A", "B"],
                         ["A", "B", "C", " "]],
                     {"A", "B", "C", "D"})
    assert s.fail_fast() is False


def test_has_unique_solution_start_false() -> None:
    s = SudokuPuzzle(4, [["C", "D", "B", "A"],
                         ["B", " ", " ", " "],
                         ["D", " ", " ", " "],
                         ["A", " ", " ", " "]],
                     {"A", "B", "C", "D"})

    assert s.has_unique_solution() is False


def test_has_unique_solution_start_true() -> None:
    s = SudokuPuzzle(4, [["C", "D", "B", "A"],
                         ["B", "A", "D", "C"],
                         ["D", "C", "A", "B"],
                         ["A", "B", "C", " "]],
                     {"A", "B", "C", "D"})
    assert s.fail_fast() is False
    assert s.has_unique_solution() is True


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

def bruh():
    import pytest
    pytest.main(['bitch.py'])


bruh()
#exp_tree_not_solvable()
# TODO BFS DOESN'T GIVE SHORTEST SOLUTION??
# TODO DFS DOESN'T EITHER LOL OH WAIT ITS ALBERTS FAULT AHHHHH
# implement the checker method which basically takes every gamestate in a
# solution and checks if the next gamestates are already in its extensions
# and removes them if it is.
# REMEMBER TO DELETE FROM THE BACK
# REMEMBER TO SEARCH EVERY FUTURE GAMESTATE AND STOP SEARCHING ONLY IF
# YOU CANT REACH IN EXTENSIONS ANYMORE
# no just don't add to gamestate if nongism
