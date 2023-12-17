## BOOK: Python Porichiti - Chapter 06

i = 1
while i <= 10:
    print (i)
    i += 1


# Fibbonacci Generator

print('Fibbonacci Generator')

fib_1, fib_2 = 0, 1
while fib_2 < 100:
    print(fib_2)
    fib_1, fib_2 = fib_2, fib_1 + fib_2

vowels = ['a', 'e', 'i', 'o', 'u']
for ch in vowels:
    print(ch)

for i in range(10):
    print(i)
    if i > 5:
        break
print(' up break, down continue ')
for i in range(10):
    if i < 5:
        continue
    print(i)
