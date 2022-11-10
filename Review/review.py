# Write a short program that prints each number from 1 to 100 on a new line. 
#  For each multiple of 3, print "Fizz" instead of the number. 
# For each multiple of 5, print "Buzz" instead of the number. 
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

for i in range(1,101):
    if i % 3 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 ==0:
        print('Buzz')
    else:
        print(i)

def checksNum(num):
    if num % 15 ==0:
        return 'fizzbuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 ==0:
        return 'Buzz'
    else:
        return num

