from typing import List
import random


def main():
    stacks = [1, 3, 5, 8]
    draw(stacks)
    turn: int = 1 if ask_for_start() else 0

    game_ending = False

    while (not game_ending):
        if turn == 1:
            stacks = player_move(stacks)
        else:
            stacks = pc_move(stacks)

        draw(stacks)
        print(f'nimsum: {nimsum(stacks)}')
        turn = (turn + 1) % 2
        game_ending = is_end(stacks)
        print("-----------------")

    if turn == 1:
        print("You have lost the game")
    else:
        print("You have won the game")


def player_move(stacks: List[int]) -> List[int]:
    row = ask_for_row(stacks)
    amount = ask_for_amount(stacks, row)

    stacks[row] -= amount
    return stacks


def pc_move(stacks: List[int]) -> List[int]:
    orders = gen_rand_list(len(stacks))
    for order in orders:
        if stacks[order] > 0:
            amount_orders = gen_rand_list(stacks[order] + 1)
            for amount_order in amount_orders:
                s = stacks[:]
                move_print = f'remove on col: {order} {amount_order} amount'
                s[order] = s[order] - amount_order
                if nimsum(s) == 0:
                    print(move_print)
                    return s
    print("No move made we have an error")


def nimsum(stacks: List[int]) -> int:
    result = 0
    for stack in stacks:
        result = result ^ stack
    return result


def is_end(stacks: List[int]) -> bool:
    return all(x <= 0 for x in stacks)


def ask_for_start() -> bool:
    answer = input("Do you want start? (y/n) ").strip()
    if answer == "y":
        return True
    if answer == "n":
        return False
    return ask_for_start()


def ask_for_row(stacks: List[int]) -> int:
    row = input("Witch row you choose? ")
    if row.isdigit():
        row = int(row)
        if 0 <= row < len(stacks):
            if stacks[row] > 0:
                return row
    return ask_for_row(stacks)


def ask_for_amount(stacks: List[int], row: int) -> int:
    amount = input("Enter your amount: ")
    if amount.isdigit():
        amount = int(amount)
        if stacks[row] - amount >= 0:
            return amount
    return ask_for_amount(stacks, row)


def gen_rand_list(length: int) -> List[int]:
    l = list(range(length))
    random.shuffle(l)
    return l


def draw(stacks: List[int]):
    for i in range(0, len(stacks)):
        stack = stacks[i]
        print(f'{i}: ', end='')
        for _ in range(stack):
            print("| ", end="")
        print()


if __name__ == "__main__":
    main()

# 0 |
# 1 | | |
# 2 | | | | |
# 4 | | | | | | | |
