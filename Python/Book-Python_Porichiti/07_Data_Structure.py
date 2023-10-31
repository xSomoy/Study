## BOOK: Python Porichoy - Chapter 07

# List
print('List:-')

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
stack.append(4)
print(stack)
stack.pop(0)
print(stack)
even = []
for item in li:
    if item % 2 == 0:
        even.append(item)
print(even)
odd = []
for item in li:
    if item % 2 == 1:
        odd.append(item)
print(odd)


# Tuple
print('Tuple:-')


tpl = (1,2,3, [1,2,3])
print(tpl[3][2])
print(type(tpl))
tpl1 = (1,2,3,'string',3.5)
for item in tpl1:
    print(item)
# Set
tpl = (1,2,3,4,5,)
a = set(tpl)
print(type(a))
print(a)

li = [2,3,5,7]
b = set(li)
print(b)
print(a & b)
print(a | b)
print(a ^ b)
print(7 in a)
print(7 in b)
c  = set('abcd')
print(c)
li = [1,2,3,4,4,5,2,3,4,5,6,7,8]
d = set(li)
print(d)
li = list(d)
print(li)

# Dictionary
print('Dictionary:-')

dt = {'a':'A', 'b':'B'}
print(dt['a'])
result = {1 : 90, 2 : 95, 3 : 98}
print(result[3])
div = {
        'Dhaka' : 10,
        'Chittagong' : 15,
        'Sylhet' : 8,
        'Khulna' : 20,
        'Rajshahi' : 12,
        'Rangpu' : 10,
        'Barishal' : 8,
        }
print(div['Dhaka'])
print(type(div))
div['Dhaka'] = 15
del div['Khulna']
print(div)
div['Khulna'] = 20
print(div)
for item in div:
    print(item)
for item in div :
    print(item , div[item])
print(div.keys())
for key in div.keys():
    print(div[key])

print(type(div.keys()))

for key, value in div.items(): #interitems doesn't work
    print(key, value)

for x in div.items():
    print(x)
