def insert_ord_1(num, lst):
    """
    Takes a number num and an ordered list of integers.  Returns another ordered list of integers
    that contains num. This version does not update lst.
    """
    if lst == []:
        res_list = [num]
    elif num >= lst[len(lst)-1]:         # check if num is greater than every thing
        res_list = lst + [num]
    else:
        for index in range(len(lst)):
            if num < lst[index]:         # check if num is smaller than the current position
                index +=1
                res_list = lst[:index-1] + [num] + lst[index-1:]
                break
    return res_list


def insert_ord_3(num, lst):
    """
    Insert at the right place a number num into an ordered list lst (ascending order).
    This version update the parameter list and is written in a pythonic way.  
    No explicit return is required because no return value is actually returned.
    If no explicit return statement is provided then Python returns the valua None.
    """

    if not lst:                            # check if the list is empty
        lst.insert(0,num)                  # insert num 
    else:
        if num >= lst[len(lst)-1]:         # check if num is greater than every thing
            lst.append(num)                # append num to the list (after all the elements)
        else :
            for index in range(len(lst)):  # loop over the whole list
                if num <= lst[index]:      # check if num is smaller than the current position
                    lst.insert(index, num) # insert before 
                    break                  # quit the for loop


def insert_ord_2(num, lst):
    """
    Insert at the right place a number num into an ordered list lst (ascending order).
    This version update the parameter list and is written in a more classic way.
    No explicit return is required because no return value is actually returned.
    If no explicit return statement is provided then Python returns the valua None.
    """  

    if lst == []:
        lst.insert(0,num)                      # insert into empty list
    else:
        done = False
        index = 0
        while (not done and index < len(lst)): 
            if num <= lst[index]:              # insert at the right place (before)
                lst.insert(index, num)
                done = True
            index += 1
        if not done:
            lst.append(num)                    # insert at the end


def main():
    """ Launcher """
    num =  int(input("Input an int: "))
    print

    lst = [3, 6, 10, 10, 20]
    print("Insert {} in {}".format(num, lst))
    print("Gives {}".format(insert_ord_1(num, lst)))
    print

    lst = [3, 6, 10, 10, 20]
    print("Insert {} in {}".format(num, lst))
    print(insert_ord_2(num, lst))
    print("gives {}".format(lst))
    print

    lst = [3, 6, 10, 10, 20]
    print("Insert {} in {}".format(num, lst))
    insert_ord_3(num, lst)
    print("gives {}".format(lst))
    print

   
if __name__ == "__main__":
    main()
