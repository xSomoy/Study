# Sololearn Challenge - Password Validation
# Recruitment [ Min ( 7 Char + 2 Digit + 2 Special ) ]

import re
password = input("Your Password Is ")
regex = r"^(?=(.*\d){2})(?=.*[a-zA-Z])([0-9a-zA-Z!@#$%&*]{2})([0-9a-zA-Z!@#$%&*]{7,})"
if re.fullmatch( regex, password):
    print("Strong")
else:
    print("Weak")