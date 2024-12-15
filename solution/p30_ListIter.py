class ListIter:
	def __init__(self, lst):
		self.lst = lst

	def __iter__(self):
		return iter(self.lst)

        
def main():
    """ Launcher """
    l = ListIter([2,5,7])
    print(l.lst)

    for x in l:
        print(x)

if __name__ == "__main__":
    main()
