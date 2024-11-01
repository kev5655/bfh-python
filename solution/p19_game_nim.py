from typing import List

from sqlalchemy.sql.operators import truediv


def main():
    stacks = [1,3,5,7]
    draw(stacks)
    print(nimsum(stacks))
    user_starts = ask_user_for_start()
    if user_starts:
        my_turn(stacks)
        pass
    else:
        pass

def my_turn(stacks) -> List[int]:
    col = ask_for_colum(stacks)
    amount = ask_for_amount(stacks, col)

    stacks[col] = stacks[col] - amount

    draw(stacks)
    return stacks

def ask_for_colum(stacks):
    col = input(f'Enter you colum [0-{len(stacks)-1}]: ')
    if col.isdigit():
        col = int(col)
        if 0 <= col < len(stacks):
            return col
    ask_for_colum(stacks)

def ask_for_amount(stacks: List[int], col: int) -> int:
    amount = input("How may stones you want to remove? ")
    if amount.isdigit():
        amount = int(amount)
        if (stacks[col] - amount) >= 0:
            return amount
        else:
            print("Not enough stones to remove.")
    ask_for_amount(stacks, col)


def nimsum(stacks) -> int:
    result = stacks[0]
    for stack in range(1, len(stacks)):
        result = result ^ stacks[stack]
    return result

def draw(stacks: List[int]):
    for i in range(0, len(stacks)):
        stack = stacks[i]
        print(f'{i} - ', end='')
        for _ in range(stack):
            print('| ', end='')
        print()

def ask_user_for_start() -> bool:
    user_starts = input("Do you want to start? (y/n)").strip()
    if user_starts == 'y':
        return True
    elif user_starts == 'n':
        return False
    else:
        ask_user_for_start()



if __name__ == "__main__":
    main()