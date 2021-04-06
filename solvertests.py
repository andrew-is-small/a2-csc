from sudoku_puzzle import SudokuPuzzle
from word_ladder_puzzle import WordLadderPuzzle, EASY, TRIVIAL
from expression_tree import ExprTree, construct_from_list
from expression_tree_puzzle import ExpressionTreePuzzle
from solver import BfsSolver, DfsSolver

"""Tests a lot of stuff honestly"""


# #### BITCH.PY TESTS REDONE #### #
def test_basic_sudoku():
    a = BfsSolver()
    c = DfsSolver()
    s = SudokuPuzzle(4,
                     [["A", "B", "C", "D"],
                      ["C", "D", " ", " "],
                      [" ", " ", " ", " "],
                      [" ", " ", " ", " "]], {"A", "B", "C", "D"})
    longst = [a.solve(s), c.solve(s)]
    for i in longst:
        assert i[0] == s
        assert i[-1].is_solved()


def test_wl():
    # both solvers, repeats and yeah
    a = BfsSolver()
    d = DfsSolver()
    b = WordLadderPuzzle("cost", "save",
                         {"cost", "cyst", "cest", "cist", "cxst", "clst",
                          "case", "cave", "sive", "sove", "save", "cast"})
    bongst = [a.solve(b), d.solve(b)]
    assert len(bongst[0]) == 5
    for i in bongst:
        assert i[0] == b
        assert i[-1].is_solved()


def test_diff():
    b = WordLadderPuzzle("cost", "savi",
                         {"cost", "cyst", "cest", "cist", "cxst", "savi",
                          "case", "cave", "sive", "sove", "save", "cast"})
    d = WordLadderPuzzle("cost", "cilm",
                         {"cost", "cyst", "cest", "cxst", "savi",
                          "case", "cave", "sive", "sove", "save", "cilm"})
    assert b.get_difficulty() == 'hard'
    assert d.get_difficulty() == 'impossible'


def test_exp_tree_ex():
    puz = WordLadderPuzzle("done", "done", {"done"})
    assert puz.get_difficulty() == 'trivial'


# #### GENERAL TESTS #### #
def test_already_solved():
    a = WordLadderPuzzle('save', 'save')
    t = ExprTree(3, [])
    p = ExpressionTreePuzzle(t, 3)
    d = DfsSolver()
    b = BfsSolver()
    s1 = d.solve(a)
    s2 = d.solve(p)
    s3 = b.solve(a)
    s4 = b.solve(p)
    assert len(s1) == 1 and s1[0] == a
    assert len(s2) == 1 and s2[0] == p
    assert len(s3) == 1 and s3[0] == a
    assert len(s4) == 1 and s4[0] == p


def test_no_solution_wl():
    a = WordLadderPuzzle('save', 'sact', {'save', 'syve', 'sact'})
    d = DfsSolver()
    b = BfsSolver()
    assert len(d.solve(a)) == 0 and len(b.solve(a)) == 0


def test_wl_extensions():
    b = WordLadderPuzzle("cost", "case",
                         {"cost", "cast", "yost", "cose",
                          "case", "cyst", "colt"})
    # so it should go 3(cast/cose), 2 cyst, 1 yost, 1 colt
    mext = b.extensions()
    ext = []
    assert len(mext) == 5
    for i in mext:
        ext.append(i.from_word)
        assert i.to_word == "case"
    assert ext[0] in ["cast", "cose"] and ext[1] in ["cast", "cose"]
    assert ext[2] == "cyst"
    assert ext[3] in ["yost", "colt"] and ext[4] in ["yost", "colt"]


# word ladder from word has to be = len to word (precondition) btw
def test_one_move():
    a = WordLadderPuzzle('save', 'cave')
    t = ExprTree('a', [])
    b = ExpressionTreePuzzle(t, 3)
    d = DfsSolver()
    bf = BfsSolver()
    s1 = [bf.solve(a), bf.solve(b)]
    s2 = [d.solve(a), d.solve(b)]
    for i in s1:
        assert len(i) == 2
        assert i[1].is_solved()
    assert len(s2[1]) == 2
    assert s2[1][1].is_solved()
    for i in s2:
        assert i[-1].is_solved()


# #### WORD LADDER PUZZLE
def test_sols_or_smth():
    a = WordLadderPuzzle('stair', 'cased')
    sol = [DfsSolver(), BfsSolver()]
    lst = []
    print("solving")
    for solver in sol:
        lips = solver.solve(a)
        lst.append(lips)
        print("solved one time, length =", len(lips))
        print("solved by", solver)
    # wanna make sure list length is either 0
    for solution in lst:
        if len(solution) == 0:
            continue
        for i in range(len(solution)):
            print(solution[i])
            if i > 0:
                assert solution[i] in solution[i - 1].extensions()
        print("############")
        assert solution[-1].is_solved()
        assert solution[0] == a


# #### EXPRESSION TREE
def test_construct_from_list():
    c = construct_from_list([['+'], ['a', 3, '*', '+'], ['b', 'c'], ['d', 1]])
    mult_tree = ExprTree('*', [ExprTree('b', []), ExprTree('c', [])])
    plus_tree = ExprTree('+', [ExprTree('d', []), ExprTree(1, [])])
    mein = ExprTree('+',
                    [ExprTree('a', []), ExprTree(3, []), mult_tree, plus_tree])
    assert c == mein


def test_construct_from_list2():
    c = construct_from_list([[3]])
    a = ExprTree(3, [])
    assert c == a


# #### SUDOKU
def test_already_solved_sudoku():
    s4 = SudokuPuzzle(4,
                      [["B", "D", "A", "C"],
                       ["C", "A", "B", "D"],
                       ["A", "C", "D", "B"],
                       ["D", "B", "C", "A"]], {"A", "B", "C", "D"})
    lst = [BfsSolver(), DfsSolver()]
    for solver in lst:
        solution = solver.solve(s4)
        assert solution[-1].is_solved()
        assert solution[0] == s4
    print("testing the hard one")
    # fixed bug where dfssolver tests if puzzle is solved before puzzle in seen
    assert s4.is_solved()
    assert s4.has_unique_solution()


# test no solution, badly placed thingies
def test_no_sol_sudoku():
    s3 = SudokuPuzzle(4,
                      [["B", "D", "A", "C"],
                       ["C", "A", "B", "D"],
                       ["A", "B", " ", "B"],
                       ["D", "C", " ", " "]], {"A", "B", "C", "D"})
    assert not s3.has_unique_solution()
    s3 = SudokuPuzzle(4,
                      [["C", "C", "A", "C"],
                       ["C", "A", "C", "D"],
                       ["C", "C", " ", "B"],
                       ["D", "C", " ", " "]], {"A", "B", "C", "D"})
    assert not s3.has_unique_solution()


def tezt():
    import pytest
    pytest.main(['solvertests.py'])


# (for wordladderpuzzle cuz i implemented a new function yea)
# test_basic_sudoku()
# test_wl()
# test_diff()
# test_no_solution_wl()
# test_wl_extensions()
# test_one_move()
# test_already_solved_sudoku()
# test_construct_from_list2()
a = True
if a:
    print("testing all...")
    tezt()
