#palindrome = input("Enter a word to check if it's a palindrome: ")
#for word in palindrome:
 #   if word == reversed(word):
  #      print('yes')

primeNumber = input('Check if your number is prime: ')
for i in primeNumber:
    if i%primeNumber==0 or i%primeNumber==1:
        print('yes')