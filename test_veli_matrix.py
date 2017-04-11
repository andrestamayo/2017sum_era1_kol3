import unittest
from matrix import Matrix

class MyTest1(unittest.TestCase):
    """docstring for MyTest1."""
    def setUp(self):
        self.l= [[1,2],[3,4]]
        self.m = Matrix(self.l)
        self.m2=Matrix([1,2],[3,4])

    def test_init(self): #it only create the matrix in a propper way when you provide the imput as a list of lists, it should work providing several lists
        self.assertEqual(self.l, self.m.m)
        self.assertEqual(self.l, self.m2.m)

class MyTest2(unittest.TestCase):
    """docstring for MyTest1."""
    def setUp(self):
        self.l= [[1,2],[3,4]]
        self.m = Matrix(self.l)


    def test_init(self): #it makes line jumps before and after each matrix repr this is unnecessary
        self.assertEqual('\n| 1 2 |\n| 3 4 |\n', self.m.__repr__())
class MyTest3(unittest.TestCase):
    """docstring for MyTest1."""
    def setUp(self):
        self.l= [[1,2],[3,4]]
        self.m = Matrix(self.l)


    def test_init(self): #it makes line jumps before and after each matrix repr this is unnecessary
        self.assertEqual('\n| 1 2 |\n| 3 4 |\n', self.m.__repr__())

class MyTest4(unittest.TestCase):
    """docstring for MyTest3."""
    def setUp(self):
        self.l= [[1,2],[3,4]]
        self.l2=[[0,0],[0,0]]
        self.l3=[[1]]
        self.m = Matrix(self.l)
        self.m1=Matrix(self.l2)
        self.m3=Matrix(self.l)
        self.m4=Matrix(self.l3)

    def test_init(self): #a matrix with the same components than other one should be the same

        self.assertEqual(self.m3,self.m+self.m1)
        self.assertEqual(self.m3,self.m1+self.m)

class MyTest5(unittest.TestCase):
    """docstring for MyTest5."""
    def setUp(self):

        self.l2=[[0,0],[0,0]]
        self.l3=[[1]]

        self.m1=Matrix(self.l2)

        self.m4=Matrix(self.l3)

    def test_init(self): #When making an erroneous addition we should give propper information to user
        self.assertRaises(ArithmeticError, self.m1.__add__,self.m4)

class MyTest6(unittest.TestCase):
    """docstring for MyTest3."""
    def setUp(self):
        self.l= [[1,2],[3,4]]
        self.l2=[[0,0],[0,0]]

        self.m = Matrix(self.l)
        self.m1=Matrix(self.l2)
        self.m3=Matrix(self.l)


    def test_init(self): #a matrix with the same components than other one should be the same

        self.assertEqual(self.m3,self.m-self.m1)
        self.assertEqual(self.m3,self.m1-self.m)
class MyTest7(unittest.TestCase):
    """docstring for MyTest3."""
    def setUp(self):
        self.l= [[1,2],[3,4]]
        self.l2=[[0,0],[0,0]]

        self.m = Matrix(self.l)
        self.m1=Matrix(self.l2)
        self.m3=Matrix(self.l)
        self.m4=Matrix(self.l2)


    def test_init(self): #a matrix with the same components than other one should be the same

        self.assertEqual(self.m4,self.m.prod(self.m1))
        self.assertEqual(self.m4,self.m1.prod(self.m))
class MyTest8(unittest.TestCase):
    """docstring for MyTest3."""
    def setUp(self):
        self.l= [[1,2],[3,4]]
        self.l2=[[0,0],[0,0]]

        self.m = Matrix(self.l)
        self.m1=Matrix(self.l2)
        self.m3=Matrix(self.l)
        self.m4=Matrix(self.l2)


    def test_init(self): #a matrix with the same components than other one should be the same

        self.assertEqual(self.m,self.m3+0)
        self.assertEqual(self.m,0+self.m3)
