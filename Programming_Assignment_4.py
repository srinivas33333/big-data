# program to factorial number
num = int(input('enter a number: '))

fact = 1
for x in range(num,0,-1):
   fact *=x

print('--factorial--',fact)


# display multiplication table
print('---table----')
for x in range(11):
    print(num,'x',x,'=',num*x)

# fibnocci number
fib_length = num
a=0
b=1

print('----fibnoci----')
print(a,b,end=' ')
while(fib_length-2 > 0):
    nt = a+b
    a = b
    b= nt
    print(nt,end=' ')
    fib_length-=1

print('----fibnoci end----')

#armstrong number
import math
print('---armstrong number----')
armstrong_num = num
arm_sum = 0
arm_lenght = len(str(armstrong_num))
if(arm_lenght  == 3 ):
    while (armstrong_num>0):
        last_d = armstrong_num % 10
        arm_sum+= int(math.pow(last_d,arm_lenght))
        armstrong_num = armstrong_num//10
        print(type(arm_sum),'-arm_sum--')

    if(num == int(arm_sum)):
        print(num,'is armstrong number')
    else:
         print('{} not an armstrong number'.format(num))
else:
    print('{} is not armstrong. please enter a three digit number'.format(armstrong_num))


#sum of natural numbers
natural_sum =0
if(num>0):
    for x in range(1,num+1):
        natural_sum+=x
    print(natural_sum,'-----sum of natural numbers----')
else:
    print('please enter a natural number.')
