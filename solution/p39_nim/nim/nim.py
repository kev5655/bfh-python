"""
Module that contains the main program for the game of Nim.


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

from random import randint
import copy

from game import Game

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
    Asks the player on which row and how many matches he/she wants to remove.
    The game is then updated
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