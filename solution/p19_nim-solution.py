# to be able to specify type annotations and static type checker mypy
from typing import Any

from random import randint
import copy

"""
This game of NIM consists of 16 matches in 4 rows arranged as follows:

          1-   |
          2-   | | |
          3-   | | | | |
          4-   | | | | | | |

The players alternately pick a certain number of matches (at least 1) in only one row,
and the one who takes the last matches wins.

A winning game (for the player who has to play) is a game for which the result of
the Vertical XOR is Non False (True value are in the result of the Vertical XOR),
otherwise it is a loosing game (only False value in the result of the Vertical XOR).
From any winning game the current player can obtain a loosing game for the other player ;-).
From any loosing game one obtains a winning game for the other player what ever one does :-(.

         Rows  Matches        Binary Conversion
          1-                        ===>          F F F
          2-   | | |                ===>          F T T
          3-   | | | | |            ===>          T F T
          4-   | | | | | | |        ===>          T T T

                                                  | | |   Vertical XOR
                                                  v v v
                                                  
                                                  F T T   Non False = "winning"
          F = False, T = True

The Game is represented by a list of integers and the Binary Convertion is done with a 
list of booleans. A the beginning the pyramid of matches, the Rows of a Game is [1,3,5,7] for example.
"""

class Game:
    """
    A game is represented by a list of integers where each element of the list represents
    the number of matches of the corresponding row.
    """

    def __init__(self) -> list[int]:
        """
        Creates a game of 4 rows.
        The max number of matches is 7 which can be represented in binary with 3 bits
        """
        self.game = [1,3,5,7]


    def int_to_bin_mod8(self, num_matches: int) -> list[bool]:
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
            0: [False, False, False],    # 000
            1: [False, False, True],     # 001
            2: [False, True,  False],    # 010
            3: [False, True,  True],
            4: [True , False, False],
            5: [True,  False, True],
            6: [True,  True,  False],    # 110
            7: [True,  True,  True]      # 111
        }
        dic_length = len(int_bin_converter)
        num_matches = num_matches % dic_length
        return int_bin_converter[num_matches]

    def game_to_bin(self) -> list[list[bool]]:
        """
        Converts a game into binary, i.e. each row of the game is converted into binary,
        it means that a list of list of booleans is provided (each element of the list
        is a row converted into binary).
        :return: a list of list of booleans
        """
        converted_game = []
        for row in self.game:
            converted_game.append(self.int_to_bin_mod8(row))
        return converted_game

    def row_to_col(self, lst_lst: list[list[Any]]) -> list[list[Any]]:
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
        # number of lines and colums of the source list
        nline = len(lst_lst)
        ncol  = len(lst_lst[0])
        # creation of the destination list where nline and ncol are permutated
        # first the list is empty
        res_lst_lst = []
        # then elements are added
        for j in range(len(lst_lst[0])):
            res_lst_lst = res_lst_lst + [list(range(nline))]
        # res_lst_lst is the destination that contains dummy values
        # copy the source list into the destination list permutating the elements
        for i in range(len(lst_lst)):
            for j in range(len(lst_lst[i])):
                res_lst_lst[j][i] = lst_lst[i][j]
        return res_lst_lst

    def is_winning(self) -> bool:
        """
        Determines whether a game is a "winning" game or not.  A game is winning
        if the result of the Vertical XOR contains some bits set to True.
        :return: True if winning, False otherwise
        """

        # converts game into binary and the converts/permutes the row and col
        game_bin_row_col = self.row_to_col(self.game_to_bin())

        res_vert_xor = []
        for i_lst in game_bin_row_col:
            res = i_lst[0]           # result is initialized to the first element of the i_th sub-list
            for j in i_lst[1:]:      # i_lst[1:] is the sub-list without the first element
                res= res ^ j         # computes the xor between to consecutive elements
            res_vert_xor.append(res)

        result = False
        for i in res_vert_xor:
            result = i or result

        return result

    def is_finished(self) -> bool:
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

def display_game(g: Game) -> None:
    """
    Displays the current game as rows of matches.
    For every row the row number is displayed followed by the matches.
    :param g: game (object) to display
    """
    print()
    row = 0
    while(row < len(g.game)):
        print(row+1, end="- ")
        m = g.game[row]
        while m > 0:
            print("| ", end='')
            m -= 1
        row += 1
        print()
    print()


def remove_one_match_random(g: Game) -> None:
    """
    Finds randomly a row on which one match can be removed.
    The game parameter is updated.
    :param g: game to update
    """
    # a way to simulate REPEAT ... UNTIL cond
    while True:
        row = randint(1, len(g.game))
        if g.game[row-1] >= 1:
            g.game[row-1] -= 1
            break
    print("1 match on row {} has been removed.".format(row))


def remove_from_winning(g: Game) -> None:
    """
    Find randomly some matches and a row to provide a loosing game to the other player.
    The game parameter is updated.
    We have the guarantee that the loop is not infinite if the game is not loosing.
    :param g: game (object) to update
    """
    while True:
        game_copy = copy.deepcopy(g)
        row = randint(1, len(game_copy.game))
        if game_copy.game[row-1] < 1:
            continue
        matches = randint(1, game_copy.game[row-1])
        game_copy.remove_matches(
            row - 1, matches)
        if not game_copy.is_winning():
            g.remove_matches(row - 1, matches)
            break
    print("{} matches on row {} have been removed.".format(matches, row))


def computer_turn(g: Game) -> None:
    """
    The strategy is as follows:
    If the current game is winning then find a row and some matches to remove such that a loosing
    game can be provided to the other player. It is guaranteed that from a winning game a loosing
    game exist.
    If the current game is loosing we cannot always remove matches on a row to find a losing game.
    Actually only one match is randomly removed to maximise the mistakes of the other player.
    :param g: current game
    """
    if g.is_winning():
        remove_from_winning(g)
    else:
        remove_one_match_random(g)


def user_turn(g: Game) -> None:
    """
    Ask the player on which row and how many matches he/she wants to remove.
    The game parameter is updated.
    :param game: the current game
    """
    while True:
        matches = int(input("Enter the number of matches to remove            : "))
        if matches < 1:
            print("   You must remove at least one match")
            continue
        row     = int(input("Enter the row on which matches have to be removed: "))
        # verify that row and matches are OK (not out-of-bounds)
        if row < 1 or row > len(g.game):
            print("   The row {} is out of bound".format(row))
            continue
        if matches > g.game[row-1]:
            print("   There are not enough matches on row {}.".format(row))
            continue
        break
    g.remove_matches(row-1, matches)


def main() -> None:
    """ Main program of the game of Nim. """
    # the current game is initialized with 1, 3, 5, 7 matches on the 4 rows.
    g = Game()

    print("\nGame of Nim")
    print(  "===========")
    display_game(g)
    start = input("Do you want to start? (y/n) ")
    print()
    if start=="y" or start=="Y":
        print("Your turn")         # player turn if the player want to start
        user_turn(g)
        display_game(g)
    while True:                    # alternatively: computer turn then player turn
        print("My turn")           # computer turn
        computer_turn(g)
        display_game(g)
        if g.is_finished():
            print("I WON\n")
            break
        print("Your turn")         # player turn
        user_turn(g)
        display_game(g)
        if g.is_finished():
            print("YOU WON\n")
            break

if __name__ == '__main__':
    main()
