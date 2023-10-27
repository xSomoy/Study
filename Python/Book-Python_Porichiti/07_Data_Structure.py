## BOOK: Python Porichoy - Chapter 0

# List

li = [1,2,3,4,5,6,7,8]
print(li)
li.reverse()
print(li)
li.sort()
print(li)
li.append(9)
print(li)
li.insert(0, 0)
print(li)
li.insert(0, -1)
print(li)
li2 = [*range(10, 21)]
print(li2)
li.extend(li2)
print(li)
print(li.count(9))
li.remove(5)
print(li)
li.pop(0)
print(li)
li3 = [0] * 5
print(li3)
li1 = li2
li2[0] = 9
print(li1)
stack = []
stack.append(2)
stack.append(3)
print(stack)
