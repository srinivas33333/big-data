# 1. Write a Python Program to Find LCM?

def twoNumLcm(a,b):

    hcf = a if a<b else b
    for i in range(1, hcf+1):
       if(a%i==0) and (b%i==0):
        hcf =i
      
    return int(a*b/hcf)

print(twoNumLcm(57,6),'--lcm of two numbers ---')

### 2. Write a Python Program to Find HCF?

def twoNumHcf(a,b):
    
   hcf =  a if a<b else b
   for i in range(1,hcf+1):
        if(a%i==0) and (b%i==0):
            hcf = i
   return hcf
    

print(twoNumHcf(52,24),'--hcf of two numbers ---')

### 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

def convert(num):
    print('binary:',bin(num))
    print('octal:',oct(num))
    print('hexadecimal:',hex(num))

convert(1)

### 4. Write a Python Program To Find ASCII value of a character?

try:
    char = input('enter a single character only:')
    ASCII = ord(char)
    print('ascii value of {} is {}'.format(char,ASCII))
except Exception as e:
    print(e,'---for your entered value for ascii--')
