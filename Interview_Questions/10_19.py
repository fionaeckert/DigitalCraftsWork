# Write a password generator in Python. User should be able to pick the strength of the password.
# Medium: At least 1 uppercase letter and 1 number, min length 8 chars
# Hard: At least 1 uppercase letter and 1 number, 1 special character min length 12 chars
# Absurd: At least 1 uppercase letter and 1 number,  1 special character min length 16 chars, password cannot have been used as of the users previous 3 passwords

import string
import random


absurdPW = []

strength = input('Please enter the strength of password you want to generate: ')
if type(strength) != str or strength != 'Medium' or strength != 'medium' or strength != 'Hard' or strength != 'hard' or strength != 'Absurd' or strength != 'absurd':
    print('Please enter one of the following: medium, hard, or absurd.')
def passwordGen(strength:str)->str:
    password = ''
    if strength == 'Medium' or strength == 'medium':
        s = 10
        password = password.join(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.punctuation, k=s))
    if strength == 'Hard' or strength == 'hard':
        s = 15
        password = password.join(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits, k=s))
        print(password)
    if strength == 'Absurd' or strength == 'absurd':
        s = 20
        password = password.join(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits, k=s))
        print(password)
        absurdPW.append(password)
passwordGen(strength)

