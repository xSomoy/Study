# You need to write a function that takes multiple words as its argument 
# and returns a concatenated version of those words separated by dashes (-).
# The function should be able to take a varying number of words as the argument.

#Solution:

def concatenate(*args):
    result = None
    for i in args:
        if result == None:
            result = i
        else:
            result += "-" + i
    return result

print(concatenate("I", "love", "Python", "!"))