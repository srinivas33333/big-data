### 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

def recusiveFeb(a,b,c):
    if c > 0:
        c = c-1
        print(a,end=' ')
        temp = b
        b = a+b
        a = temp
        recusiveFeb(a,b,c)

print(recusiveFeb(0,1,4),'----febnosie---')

### 2. Write a Python Program to Find Factorial of Number Using Recursion?

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3),'-----factorial-')

### 3. Write a Python Program to calculate your Body Mass Index?

def bmi(weight,height):
    return weight/height**2

print(bmi(70,1.8),'----bmi---')


### 4. Write a Python Program to calculate the natural logarithm of any number?

import math

try:
    # num = int(input("Enter the number: "))
    num = 3
except Exception as e:
    print(e,'---logarithm---')
else:
    print(math.log(num),'------logarithm---')


### 5. Write a Python Program for cube sum of first n natural numbers?
import functools
def cube(n):
    return sum(range(n+1))**3
    # sum=0
    # for i in range(1,n+1):
    #     sum+=i
    # print(sum)
    # return sum**3

print(cube(3),'---cube of sum---')
