'''
Q1. A three digit number is said to be an “Armstrong number” if the sum of the third power of its individual digits is equal to the number itself. Example: 371 is an Armstrong number as 371 = 3 3 + 7 3 + 1 3 407 is an Armstrong number as 407 = 4 3 + 0 3 + 7 3 Write a pseudo-code to check whether a given three digit number is an Armstrong number.
''' 

x = int(input("Enter your number"))
while x != abs(x):
    x = int(input("Only +ve number are acceptable, please eneter again"))
y = str(x)
y = map(int,y)           #This is a method of mapping each item of a string into integer.
y = list(y)

print("your number is Armstrong") if x == sum([number**3 for number in y]) else print("No its not Armstrong")
print("minumun digit in your three digit number was: ", min(y))
