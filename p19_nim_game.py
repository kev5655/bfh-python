from typing import List
import random


def main():
    stacks = [1, 3, 5, 8]
    draw(stacks)
    turn: int = 1 if ask_for_start() else 0
    # print(f"Player move {player_starts}")
    
    game_running = True
    
    while(game_running):
        if turn == 1:
            stacks = player_move(stacks)
        else:
            stacks = pc_move(stacks)
            print("PC")
            
        draw(stacks)
        print(f'nimsum: {nimsum(stacks)}')
        turn = (turn + 1) % 2
        game_running = is_end(stacks)
    
def player_move(stacks: List[int]) -> List[int]:
    row = ask_for_row(stacks)
    amount = ask_for_amount(stacks, row)
    
    stacks[row] -= amount
    return stacks
    
def pc_move(stacks: List[int]) -> List[int]:
    orders = gen_rand_list(len(stacks))
    print(orders)
    for order in orders:
        if stacks[order] > 0:
            amount_orders = gen_rand_list(stacks[order] + 1)
            print("")
            for amount_order in amount_orders:
                s = stacks[:]
                s[order] = s[order] - amount_order
                if nimsum(s) == 0:
                    return s
    print("No move made we have an error")

def nimsum(stacks: List[int]) -> int:
    result = 0
    for stack in stacks:
        result = result ^ stack
    return result

def is_end(stacks: List[int]) -> bool:
    return not all(x < 0 for x in stacks)
    
    
def ask_for_start():
    answer = input("Do you want start? (y/n) ").strip()
    if answer == "y":
        return True
    if answer == "n":
        return False
    ask_for_start()
    

def ask_for_row(stacks: List[int]) -> int:
    row = input("Witch row you choose? ")
    if row.isdigit():
        row = int(row)
        if 0 < row < len(stacks):
            return row
    ask_for_row(stacks)

def ask_for_amount(stacks: List[int], row: int) -> int:
    amount = input("Enter your amount: ")
    if amount.isdigit():
        amount = int(amount)
        if stacks[row] - amount >= 0:
            return amount
    ask_for_amount(stacks, row)
    
def gen_rand_list(length: int) -> List[int]:
    l = list(range(length))
    # print(l)  # Print the list before shuffling
    random.shuffle(l)  # Shuffle in place
    # print(l)  # Print the shuffled list
    return l  # Return the shuffled list

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
