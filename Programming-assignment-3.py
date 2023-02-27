### 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
num = 10

if(num > 0):
    print(num, "is Positive")
elif(num < 0):
    print(num, "is Negative")
else:
    print(num, "is Zero")

    ### 2. Write a Python Program to Check if a Number is Odd or Even?
a = 4
if(a%2 == 0): print('even')
else: print('odd')

### 3. Write a Python Program to Check Leap Year?

year = 2020

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print("Leap Year")
else:
    print("Not a Leap Year")

### 4. Write a Python Program to Check Prime Number?
##### Sol.

num = -1

isPrime = True

if num <= 1:
    print(num, "is neither prime nor composite")
else:
    d = 2
    while(d*d <= num):
        if(num%d==0):
            isPrime = False
            break
        d = d + 1

if(num > 1):
    if(isPrime):
        print(num, "is prime number")
    else:
        print(num, "is not prime number")


### 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# 1 2 3 5 7 11 13 17 23 29 31 37 41
prmeTracker = 1
print(1, 2,3,5,7, end=' ')
for i in range(1,1001):
    # print(i, end='l ')
    for x in range(prmeTracker,i+1):
    #    print(x, end=' ')
       if x == i:
           continue
       elif x == 2 or x == 1:
        #    print(x, end=' ')
           continue
       elif i%x ==0 or i%2 == 0 or i%3 == 0 or i%7 == 0 or i%5 == 0:
            break
       else:
            print(i ,end=' ')
            prmeTracker = i
            break
