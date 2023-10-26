## BOOK: Python Porichiti - Chapter 03



country = 'Bangladesh'
print(country[0])
print(country[1])
print(len(country))
country1 = 'Bangla' + 'desh'
print(country1)
print(country.find('Bangla'))
print(country.find('abc'))
print(country.find('desh'))
print(country.__len__())
print(country1.replace('Bangladesh', 'bangladesh'))
str = 'bc d '
print(str.strip())  # Only Removes the Ending white spaces
str1 = '  a  b c  d  '
print(str1.lstrip())  # Only Removes the Left White Spaces
print(str1.rstrip())  # Just Like strip()
str2 = 'AbcDeF'
print(str2.upper())
print(str2.lower())
str3 = 'Bangla'
str4 = 'desh'
print(str3, str4)
str3, str4 = str4, str3
print(str3, str4)

################### 01:56 xSomoy #########################

