# The Fibonacci sequence is one of the most famous formulas in mathematics.
# Each number in the sequence is the sum of the two numbers that precede it.
# For example, here is the Fibonacci sequence for 10 numbers, starting from 0: 0,1,1,2,3,5,8,13,21,34.

# Write a program to take N (variable num in code template) positive numbers as input,
# and recursively calculate and output the first N numbers of the Fibonacci sequence (starting from 0).


# Solution:
num = int(input())
def fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

fibonacci(num)