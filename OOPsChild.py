from OOPS import Calculator


class OOPsChild(Calculator):
    nbr = 50

    def __init__(self, p, q):
        Calculator.__init__(self, p, q)

    def testprint(self):
        print(self.nbr)

    def getcompletedata(self):
        return self.num + self.nbr + self.summing()


calcchild1 = OOPsChild(7, 5)
calcchild1.testprint()
print(calcchild1.getcompletedata())

