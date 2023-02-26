### 1. Write a Python program to convert kilometers to miles?
import calendar
import math


km = 6
m = 6/1.60934
# print("For {0} km equivalent distance in miles = {1}".format(km, m))
#
### 2.Write a Python program to convert Celsius to Fahrenheit?
c = 35

f = (9*c/5)+32

# print("For Celsius = {} equivalent Fahrenheit = {}".format(c, f))

### 3. Write a Python program to display calendar?
##### Sol.

year = 2021
month = 12

# print(calendar.month(year, month))

### 4. Write a Python program to solve quadratic equation?
a= 1
b = -9
c = 14

z = (-b+math.sqrt(b**2 - 4*a*c))/2
y = (-b-math.sqrt(b**2 - 4*a*c))/2
# print(z , y)

### 5. Write a Python program to swap two variables without temp variable?
a = 1
b = 2

a = a+b
b = a -b
a = a - b
print(a, b)