# You are given a number input, and need to check if it is a valid phone number.
# A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
# Output "Valid" if the number is valid and "Invalid", if it is not.

# Solution:

import re
pattern = r"^[1|8|9][0-9]*$"
num = input()
if re.match(pattern, num) and len(num)==8:
    print("Valid")
else:
    print("Invalid")