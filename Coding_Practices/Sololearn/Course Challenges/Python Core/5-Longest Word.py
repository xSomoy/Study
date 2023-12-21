# Longest Word
# Given a text as input, find and output the longest word.

# Solution:
txt = input()
foo = txt.split()
bar = list(sorted(foo, key = len))
print(bar[-1])


