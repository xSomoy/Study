# Code Challenge #4 By MSN [ https://www.sololearn.com/post/521050/?ref=app ]
import re
pattern = input()
regex ="[^udlr]"
# ↑ ↓ ← →
u,d,l,r,row,col= 0,0,0,0,0,0

if re.search(regex, pattern):
    print ("Invalid Input")
else:
    for i in pattern:
        if(i == 'u'): u=u+1
        if(i == 'd'): d=d+1
        if(i == 'l'): l=l+1
        if(i == 'r'): r=r+1


if (d == 0 ) & (u == 0):row=1       
elif(u>d): row = d+(u-d)
else: row = d

if (r == 0 ) & (l == 0):col=1 
elif(l>r): col = r+(l-r)
else: col = r

cRow,cCol,iCol = 0,0,0

print(row)
print(col)
while (row>=cRow):
    if (pattern[iCol] == 'd'):print('↓',)
    if (pattern[iCol] == 'u'):print('↑', end=" ")
    if (pattern[iCol] == 'l'):print('←', end=" ")
    if (pattern[iCol] == 'r'):print('→', end=" ")
    if(iCol<=col):iCol+=1
    cRow+=1
    