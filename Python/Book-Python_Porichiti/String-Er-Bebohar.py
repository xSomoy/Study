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
