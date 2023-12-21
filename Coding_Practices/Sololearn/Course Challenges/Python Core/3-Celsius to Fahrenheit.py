# You are making a Celsius to Fahrenheit converter.
# Write a function to take the Celsius value as an argument
# and return the corresponding Fahrenheit value.


# Solution:

celsius = int(input())

def conv(c):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit
    

fahrenheit = conv(celsius)
print(fahrenheit)
