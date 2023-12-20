## BOOK: Python Porichiti - Chapter 12

print('CLASS AND OBJECT\n-----------------------------------------')

class Square:
    side = 0
    def area(self):
        return self.side * self.side

sqr1 = Square()
area = sqr1.area()
print(area)
sqr1.side = 5
area = sqr1.area()
print(area)


## Instantiation

class Square:
    def __init__(self, x):
        self.side = x
    def area(self):
        return self.side * self.side

sqr2 = Square(6)
area2 = sqr2.area()

print(area2)


## Instance Object
print('\n\nINSTANCE OBJECT\n-------------------------------------')


class Square:
    side = 0
    def __init__(self, x):
        self.side = x
    def area(self):
        return self.side * self.side

sq = Square(5)
print(sq)
print(sq.side)
print(Square.side)
print(sq.area())
#print(Square.area())
print(Square.area(sq))


class Test:
    side = 0
    def __init__(obg, x):
        obg.side = x
    def area(obg):
        return obg.side * obg.side

tst = Test(2)
print(Test.area(tst))



print('\n\nINHERITANCE\n-------------------------------------------')

class Rectangle:
    def __init__(self):
        print('Inside init of Rectangle')

class Square(Rectangle):
    def __init__(self):
        print('Inside init of Square')


r = Rectangle()
sq = Square()


## Test -- Start

class A:
    def __init__(self):
        self.a = 3
    def sq(self):
        return self.a * self.a

class B(A):
    def __init__(self):
        self.a = 2

p = B()
print(p.sq())

## Test -- END


class Rectangle:
    def __init(self):
        print('Inside init of Rectangle')

    def area(self, x, y):
        return x * y

class Square(Rectangle):
    def __init__(self):
        print('Inside init of Square')

sq = Square()
print(sq.area(5,5))
