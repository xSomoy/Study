# The carousel is designed for 3 people who are each at least 16 years old.
# You are given a program that takes all 3 passengers' ages as inputs and inserts them in a list.
# Complete the program so that if it finds a value less than 16, it breaks the loop and outputs "Too young!".
# If the age requirement is satisfied, the program outputs "Get ready!".

# Solution:

ages = []
i = 0
g = 0
while i<3:
   age = int(input())
   ages.append(age)
   i+=1
   if age > 16:
       g=g+1
   else:
       g=g+0
if g > 2:
   print("Get ready!")
else:
   print("Too young!")