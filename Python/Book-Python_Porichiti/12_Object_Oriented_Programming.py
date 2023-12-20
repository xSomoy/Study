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

print('\n\nMETHOD OVERRIDING\n---------------------------------')

class Rectangle:
    def __init__(self):
        print('Inside init of Rectangle')

    def area(self, x, y):
        return x * y

class Square(Rectangle):
    def __init__(self):
        print('Inside init of Square')

    def area(self, x):
        return Rectangle.area(self, x, x)

sq = Square()
print(sq.area(5))

print('\n\nPRIVATE ATTRIBUTE\n-------------------------------')

class Square:
    pass

sq = Square()
print(sq)
print(sq.__class__)

class Square:
    area = 50
    def area(self, x):
        return x * x

sq = Square()
print(sq)
print(sq.area(5))
sq.area = 100
print(sq.area)
#print(sq.area(6))

class Square:
    def area(self, x):
        return x * x
    area = 50

sq = Square()
print(sq.area)
#print(sq.area(5))

class A:
    pass

a = A()
print(a)
print(a.__class__)

class B(A):
    pass

b = B()
print(b)
print(b.__class__)

print(isinstance(b,B))
print(isinstance(b,A))
print(isinstance(a,A))
print(isinstance(a,B))


print(issubclass(B , A))

print('\n\nITERATOR\n------------------------------')

city = 'Dhaka'

for ch in city:
    print(ch)

for x in [1,2,3,4]:
    print(x)

li = [1,2,3,4]
print(li.__iter__)

icity = iter(city)
print(icity)
print(next(icity))
print(next(icity))
print(next(icity))
ili = iter(li)
print(next(ili))
print(next(ili))


class Reverse:
    """
    Iterator for looping over aswquence backwards.
    """
    def __init__(self,data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('abcd')
print(rev)

for item in rev:
    print(item)


print('\n\nGENERATOR\n-----------------------------')

def reverse(data):
    for index in range(len(data)-1, -1,-1):
        yield data[index]

for char in reverse('abcd'):
    print(char)

gen = reverse('abcd')
print(gen)
print(type(gen))

for i in gen:
    print(i)

for i in gen:
    print(i)

def gen(n):
    i = 0 
    while i < n:
        yield i
        i += 1

x = gen(5)

print(x)
for i in x:
    print(i)




## THE END 
