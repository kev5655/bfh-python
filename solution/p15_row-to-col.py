def row_to_col(lst_lst):
    #(lst_lst: List[List[Any]]) -> List[List[Any]]:
    """
    Transforms a list of lists into another list of lists as follows
    [[x1,x2,x3],[y1,y2,y3], ...] --> [[x1,y1,...],[x2,y2,...],[x3,y3,...]]
    The function assumes that all the lists in the input list have the same number of
    elements (this assumption is important for the termination of the recursion).
    The function assumes also that the paramater is a list of lists and is not empty
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
