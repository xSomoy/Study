## METHOD 1

def string_rev(string):
    revs = []
    index = len(string) - 1
    for i in string:
        revs.append(string[index])
        index -= 1
    return ''.join(revs)

s = 'abc'
print(string_rev(s))


## METHOD 2

def string_rev(string):
    revs = ''
    index = len(string) - 1
    for i in string:
        revs += string[index]
        index -= 1
    return revs

s = 'abc'
print(string_rev(s))


