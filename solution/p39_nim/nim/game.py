"""
Module that contains the Game class which stores the 4 rows of matches and the necessary methods
"""

# to be able to specify type annotations and static type checker mypy
from typing import List, Any, Set, Dict, Tuple, Optional

from functools import reduce
from operator import __xor__, __or__

class Game:
    """
    A game is represented by a list of integers where each element of the list represents
    the number of matches of the corresponding row.
    """

    def __init__(self) -> None:
        """
        Creates a game of 4 rows.
        The max number of matches is 7 which can be represented in binary with 3 bits
        """
        self.game = [1, 3, 5, 7]

    def int_to_bin_mod8(self, num_matches: int) -> List[bool]:
        """
        Converts an integer into binary over 3 bits (modulo 8).
        Each bit is represented by a boolean. It is more logical to represent
        the bits with true/false values rather than with 0/1 integer value.
        For the sake of simplicity every constant is converted explicitly.
        :param num_matches: the integer to convert into binary
        :return: the list of booleans, each boolean represents a bit (Most Significant Bit on the left)
        """

        # dictionary used for switch-case
        int_bin_converter = {
            0: [False, False, False],  # 000
            1: [False, False, True],  # 001
            2: [False, True, False],  # 010
            3: [False, True, True],
            4: [True, False, False],
            5: [True, False, True],
            6: [True, True, False],  # 110
            7: [True, True, True]  # 111
        }
        dic_length = len(int_bin_converter)
        num_matches = num_matches % dic_length
        return int_bin_converter[num_matches]

    def game_to_bin(self) -> List[List[bool]]:
        """
        Converts a game into binary, i.e. each row of the game is converted into binary,
        it means that a list of list of booleans is provided (each element of the list
        is a row converted into binary).
        :return: a list of list of booleans
        """
        return list(map(self.int_to_bin_mod8, self.game))
        # equivalent to
        # converted_game = []
        # for row in game:
        #     converted_game.append(int_to_bin_mod8(row))
        # returne converted_game

    def row_to_col(self, lst_lst: List[List[Any]]) -> List[List[Any]]:
        """
        Transforms a list of lists into another list of lists as follows
        [[x1,x2,x3],[y1,y2,y3], ...] --> [[x1,y1,...],[x2,y2,...],[x3,y3,...]]
        The function assumes that all the lists in the input list have the same number of
        elements (this assumption is important for the termination of the recursion).
        This implementation takes advantage of map function and recursion and which makes the
        the implemention easer to develop and understand.
        :param lst_lst: the list of lists (row - col) to transform
        :return: the transformed list of lists (col - row)
        """
        head = (lambda x: x[0])
        tail = (lambda x: x[1:])
        if not lst_lst or not head(lst_lst):  # c.f. the remark about recursion termination
            return []
        else:
            return [list(map(head, lst_lst))] + (self.row_to_col(list(map(tail, lst_lst))))

    def is_winning(self):
        """
        Determines whether a game is a "winning" game or not.  A game is winning
        if the result of the Vertical XOR contains some bits set to True.
        :return: True if winning, False otherwise
        """
        # performs the Vertical XOR by reducing as list of bool (lst) with xor lambda
        reduce_xor = (lambda lst: reduce(__xor__, lst, False))

        # converts game into binary and the converts/permutes the row and col
        game_bin_row_col = self.row_to_col(self.game_to_bin())

        # performs Vertical XOR on every column
        res_vert_xor = list(map(reduce_xor, game_bin_row_col))

        # performs Horizontal OR and return
        return reduce(__or__, res_vert_xor, False)

    def is_finished(self):
        """
        Determines if a game is over by doing the sum of the rows.
        A game is over whenever there is no matches anymore.
        :return: True is the game is over, False otherwise.
        """
        return sum(self.game) == 0

    def remove_matches(self, row: int, matches: int) -> None:
        """
        Removes some matches on a given row of a given game.
        This function is not a pure function because it changes the matches of the game parameter.
        :param row: the row on which the matches have to be removed
        :param matches: the number of matches to remove
        """
        self.game[row] -= matches
