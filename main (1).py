Programiz

Search...
Programiz PRO


Python Program to Find Factorial of Number Using Recursion
To understand this example, you should have the knowledge of the following Python programming topics:

Python if...else Statement
Python Functions
Python Recursion
The factorial of a number is the product of all the integers from 1 to that number.

For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers and the factorial of zero is one, 0! = 1.

Source Code
# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
Run Code
Output

The factorial of 7 is 5040