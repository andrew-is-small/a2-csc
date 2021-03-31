"""
CSC148, Winter 2021
Assignment 2: Automatic Puzzle Solver
==============================
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Diane Horton, Jonathan Calver, Sophia Huynh,
         Maryam Majedi, and Jaisie Sin.

All of the files in this directory are:
Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh,
                   Maryam Majedi, and Jaisie Sin.

=== Module Description ===

This module contains the abstract Solver class and its two subclasses, which
find solutions to puzzles, step by step.
"""

from __future__ import annotations

from typing import List, Optional, Set

# You may remove this import if you don't use it in your code.
from adts import Queue

from puzzle import Puzzle


class Solver:
    """"
    A solver for full-information puzzles. This is an abstract class
    and purely provides the interface for our solve method.
    """

    # You may NOT change the interface to the solve method.
    # Note the optional parameter seen and its type.
    # Your implementations of this method in the two subclasses should use seen
    # to keep track of all puzzle states that you encounter during the
    # solution process.
    def solve(self, puzzle: Puzzle,
              seen: Optional[Set[str]] = None) -> List[Puzzle]:
        """
        Return a list of puzzle states representing a path to a solution of
        <puzzle>. The first element in the list should be <puzzle>, the
        second element should be a puzzle that is in <puzzle>.extensions(),
        and so on. The last puzzle in the list should be such that it is in a
        solved state.

        In other words, each subsequent item of the returned list should take
        the puzzle one step closer to a solution, which is represented by the
        last item in the list.

        Return an empty list if the puzzle has no solution.

        <seen> is either None (default) or a set of puzzle states' string
        representations, whose puzzle states can't be any part of the path to
        the solution.
        """
        raise NotImplementedError


# TODO (Task 2): implement the solve method in the DfsSolver class.
# TODO TEST BITCH2
# TODO seen is not none may not be necessary cuz we initialize seen everytime
# Your solve method MUST be a recursive function (i.e. it must make
# at least one recursive call to itself)
# You may NOT change the interface to the solve method.
class DfsSolver(Solver):
    """"
    A solver for full-information puzzles that uses
    a depth first search strategy.
    """

    def solve(self, puzzle: Puzzle,
              seen: Optional[Set[str]] = None) -> List[Puzzle]:
        """
        Return a list of puzzle states representing a path to a solution of
        <puzzle>. The first element in the list should be <puzzle>, the
        second element should be a puzzle that is in <puzzle>.extensions(),
        and so on. The last puzzle in the list should be such that it is in a
        solved state.

        In other words, each subsequent item of the returned list should take
        the puzzle one step closer to a solution, which is represented by the
        last item in the list.

        Return an empty list if the puzzle has no solution.

        <seen> is either None (default) or a set of puzzle states' string
        representations, whose puzzle states can't be any part of the path to
        the solution.
        """
        # initialize seen if it's not there
        if seen is None:
            seen = set()
        # base cases
        if puzzle.is_solved():
            return [puzzle]
        if puzzle.fail_fast() or (seen is not None and str(puzzle) in seen):
            return []
        else:
            # we don't want to see this again.
            # this only applies for word ladder so far...we don't wanna go
            # backwards
            seen.add(str(puzzle))
            for ext in puzzle.extensions():
                if self.solve(ext):
                    # list not empty
                    return [puzzle] + self.solve(ext)
            return []
        # scuffed code, run tests
        # you can assert the conditions that everything is in extensions and
        # first ting is the puzzle, last is solved. This would be good for
        # randomized tests


# TODO (Task 2): implement the solve method in the BfsSolver class.
# Hint: You may find a Queue useful here.
class BfsSolver(Solver):
    """"
    A solver for full-information puzzles that uses
    a breadth first search strategy.
    """

    def solve(self, puzzle: Puzzle,
              seen: Optional[Set[str]] = None) -> List[Puzzle]:
        """
        Return a list of puzzle states representing a path to a solution of
        <puzzle>. The first element in the list should be <puzzle>, the
        second element should be a puzzle that is in <puzzle>.extensions(),
        and so on. The last puzzle in the list should be such that it is in a
        solved state.

        In other words, each subsequent item of the returned list should take
        the puzzle one step closer to a solution, which is represented by the
        last item in the list.

        Return an empty list if the puzzle has no solution.

        <seen> is either None (default) or a set of puzzle states' string
        representations, whose puzzle states can't be any part of the path to
        the solution.
        """
        # THIS CODE IS HORRENDOUS WTF
        # I don't think it needs recursion though...? this should be ok

        # our queue will literally just be a list that we pop off of
        # we're gonna enqueue more than we dequeue, so let's
        # APPEND TO ENQUEUE, POP(0) TO DEQUEUE
        game_q = Queue()
        game_q.enqueue(puzzle)
        seen = set()
        # ####################################################
        # ok so dict will have puzzle: parent
        # this is gonna take up so much memory but please don't worry ok...
        stated = {}
        # maybe implement a dictionary that stores the thing with a numerical
        # key, and then look for it to take up less memory?? who knows LOL
        ret_lst = []

        # change the while condition
        while not game_q.is_empty():
            curr = game_q.dequeue()
            # print(curr)
            # fail
            if (seen is not None and str(curr) in seen) or curr.fail_fast():
                # fail, discard this state.
                # add to seen? I don't think we need to...
                # TODO may delete this in the future check with stuff...
                if str(curr) not in seen:
                    seen.add(str(curr))
                # delete from dict potentially
                pass
            elif curr.is_solved():
                # game is solved, return stuff!
                # we have to reverse the list later but yeah
                ret_lst.append(curr)
                while str(curr) in stated:
                    curr = stated[str(curr)]
                    ret_lst.append(curr)
                ret_lst.reverse()
                break
            # get extensions
            # - Add them to queue
            # - Add them to dict
            else:
                for puz in curr.extensions():
                    # TODO check this
                    if str(puz) not in seen:
                        game_q.enqueue(puz)
                        # LOW IQ CODE UPCOMING
                        stated[str(puz)] = curr
            # we will add it to seen because at this point we already
            # processed it, shouldn't see it again.
            # TODO: is this good? who knows?
            seen.add(str(curr))
        return ret_lst
        # use the fail_fast and is_solved puzzle methods also extensions
        # THIS CODE MAKES SENSE IN THEORY, BUT WE DEFINITELY GOTTA WRITE TESTS


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={'pyta-reporter': 'ColorReporter',
                                'allowed-io': [],
                                'allowed-import-modules': ['doctest',
                                                           'python_ta',
                                                           'typing',
                                                           '__future__',
                                                           'puzzle',
                                                           'adts'],
                                'disable': ['E1136'],
                                'max-attributes': 15}
                        )
