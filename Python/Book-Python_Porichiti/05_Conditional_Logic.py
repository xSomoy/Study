## BOOK: Python Porichiti - Chapter 05

print(type(True))
print(bool(-1))
print(bool(0))
print(bool(' '))
print(bool('as'))
a = True
print(not a)
a = 5
b = 3
if a > 0:
    print('a positive')
if b < a:
    print('affermative')
if a == b:
    print('==')
if b <= a:
    print('<=')
if a >= b:
    print('>=')
if a != b:
    print('!=')

vowels = ['a', 'e', 'i', 'o', 'u']
x = 'i'
if x in vowels:
    print(x)
else:
    print('not a vowels')
