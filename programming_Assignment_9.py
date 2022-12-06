def disarium(num):
    sum =0
    for i in range(0,(len(num))):
       
        sum += int(num[i])**(i+1)
    if(str(sum) == num):
        return True
    return False

print(disarium('135'),'--disarium number--')

### 2. Write a Python program to print all disarium numbers between 1 to 100?

for i in range(1,101):
    if disarium(str(i)) == True:
        print(i,end=' ')

print('--list of disarium numbers between 1 to 100---')
### 3. Write a Python program to check if the given number is Happy Number?

def happyNum(num):
    sum =0
    for i in range(len(str(num))):
        sum += int(str(num)[i])**2
    # print(sum,'--sum--')
    if len(str(sum)) == 1:
       
        if(sum == 1):
            return True
        elif(sum == 4):
            return False
    else:
        happyNum(sum)

print(happyNum(545))

def task3(num):

    res = num; 
    def isHappy(num):    
        r = 0;  
        s = 0
        while(num > 0):    
            r = num%10    
            s += r**2  
            num //= 10    
        return s     

    while(res != 1 and res != 4):    
        res = isHappy(res)    

    if(res == 1):    
        return True
    elif(res == 4):    
        return False
### 4. Write a Python program to print all happy numbers between 1 and 100?
for i in range(1, 101):
    if task3(i) == True:
        print(i, end = ' ')
print('')
### 5. Write a Python program to determine whether the given number is a Harshad Number?

def task5(num):
    temp = num
    total = 0
    while (temp > 0):
        total = total + (temp%10)
        temp = temp//10
        
    if num%total==0:
        print("Harshad Number")
    else:
        print("Not Harshad Number")
task5(156)

### 6. Write a Python program to print all pronic numbers between 1 and 100?

i = 0
while True:
    pronicNum = i*(i+1)
    i = i + 1
    if pronicNum > 100:
        break
    print(pronicNum, end = ' ')
print('--pronic numbers--')
