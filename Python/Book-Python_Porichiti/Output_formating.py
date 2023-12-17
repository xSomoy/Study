s = 'a b c d'
print(s.split())
#-------
s = 'a   b c    d'
print(s.split())
#-------
s = 'a+b+c+d'
print(s.split('+'))
#-------
li = ['a','b','c']
print(','.join(li))
print('+'.join(li))
print(''.join(li))
#-----
for i in range(15):
	print(str(i).rjust(2))

print('100'.rjust(10))
print('1000'.ljust(10))
print('1000'.center(10))
#------
print('12'.zfill(6))
print('-12'.zfill(6))
print('{0} vs {1}'.format('Bangladesh','Sri Lanka'))