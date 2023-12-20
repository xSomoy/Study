## BOOK: Python Porichiti - Chapter 12

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
