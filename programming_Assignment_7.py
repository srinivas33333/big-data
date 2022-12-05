### 1. Write a Python Program to find sum of array?
import functools
l = [1,2,3,-412, 123, 369, 111]
add_nums = lambda x,y:x+y
sum = functools.reduce(add_nums,l)
print(sum,'---sum of list items---')

### 2. Write a Python Program to find largest element in an array?

arrayMax = -99999999999999999999
for i in l:
    if i > arrayMax:
        arrayMax = i
print(arrayMax,'--larget array number in list --')

### 3. Write a Python Program for array rotation?

print(l[::-1],'---rotated array ---')

### 4. Write a Python Program to Split the array and add the first part to the end?
def splitAdd(l, split):
    '''
    l = list
    split = splitIndex
    '''
    # x = l[:split]
    # y = list(l[split:])
    # print(y,x)
    # z= y.extend(x)
    out = []
    for i in range(len(l)):
        index = (i+len(l)+split)%len(l)
        out.append(l[index])
    
    return  out

print(splitAdd(l, 3),'--first part array at end--')


### 5. Write a Python Program to check if given array is Monotonic?

