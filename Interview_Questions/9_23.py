# Mr. Vincent works in a door mat manufacturing company. 
# One day, he designed a new door mat with the following specifications: 
# Mat size must be X. ( is an odd natural number, and is times .) 
# The design should have 'WELCOME' written in the center. 
# The design pattern should only use |, . and - characters. 
# Constraints 5 < N < 101 15 < M < 303

l = 7
w = 21
m = '---------.|.---------'

dash = '-'
dot = '.|.'

# 21 characters in each row, split between dashes, dots, and letters
# dashes decrease by 1/3 with each step until the middle, where they start increasing
# dots increase by 2 with each step until the middle, where they start decreasing
# precisely in the middle are a number of dashes equal to the length*2 with the word WELCOME

for m in range(0,int((l-1)/2)):
    print((dash*(l+2) + dot + dash*(l+2)))



for m in range(1,2):
    print((dash*(l+2)) + dot + (dash*(l+2)))
    for m in range (2,3):
        print((dash*6) + (dot*3) + (dash*6))
        for m in range (3,4):
            print((dash*3) + (dot*5) + (dash*3))
            for m in range (4,5):
                print((dash*7)+'WELCOME'+(dash*7))
                for m in range(5,6):
                    print((dash*3) + (dot*5) + (dash*3))
                    for m in range(6,7):
                        print((dash*6) + (dot*3) + (dash*6))
                        for m in range(8,9):
                            print((dash*9) + dot + (dash*9))