# Author: Prateek Joshi

"""
Function to generate a random password
    
You can generate a random password with the specified length with restrictions on the number of digits, uppercase and lowercase letters.
    
length: Maximum number of characters in the password
digits: Minimum number of digits in the password
upper: Minimum number of upper case letters in the password
lower: Minimum no. of lower case letters in the password
    
returns: A random password with the above constaints (of type str)

"""

#!/usr/bin/env python

import string
from time import time
from itertools import chain
from random import seed, choice, shuffle


def generatePassword(length=8, digits=2, upper=2, lower=2):
    seed(time())

    letters = string.letters.strip("oO")

    password = list(
        chain(
            (choice(string.digits) for _ in range(digits)),
            (choice(string.uppercase) for _ in range(upper)),
            (choice(string.lowercase) for _ in range(lower)),
            (choice(letters) for _ in range((length - digits - upper - lower)))
        )
    )

    shuffle(password)

    return "".join(password)

print generatePassword()
print generatePassword(10)
print generatePassword(digits=4)
print generatePassword(12, upper=3)
