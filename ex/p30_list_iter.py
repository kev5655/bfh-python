
class ListIter:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return iter(self.lst)


l = ListIter([2, 5, 7])
for x in l:
    print(x)
