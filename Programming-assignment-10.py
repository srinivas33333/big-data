### 1. Write a Python program to find sum of elements in list?
l = [2, 4, 1, 5, 6, 7]
total = 0
for val in l:
    total+=val

print('--sum. array value to single value with for loop',total)

### 2. Write a Python program to  Multiply all numbers in the list?

l = [2, 4, 1, 5, 6, 7]

mul = 1
for i in l:
    mul *= i
    
print('--multiply. array value to single value with for loop',mul)

### 3. Write a Python program to find smallest number in a list?

l = [2, 0, 1, 1235, 6, -7123]

smallest = l[0]

for value in l:
    if value < smallest:
        smallest = value

print('--min with for loop',smallest)

### 4. Write a Python program to find largest number in a list?

l = [2, 0, 1, 1235, 6, -7123]

maximum = l[0]
for i in l:
    if i > maximum:
        maximum = i
        
print('--max of array with for loop',maximum)

### 5. Write a Python program to find second largest number in a list?

l = [2, 0, 1, 1235, 6, -7123]
l.sort()
print('--second largest', l[len(l)+1-len(l)])

### 6. Write a Python program to find N largest elements from a list?
print('--max of array with methods',max(l),l[len(l)-1])

### 7. Write a Python program to print even numbers in a list?
l = [2, 0, 1, 1235, 6, -7123, 21, 54, 12, -23, -42]

for value in l:
    if val//2 == 0:
        print(value)

### 8. Write a Python program to print odd numbers in a List?

print([ i for i in l if i%2 == 1], '--odd numbers')

### 9. Write a Python program to Remove empty List from List?
l = [[], 12, 31, [1,2, -23] , [1], [], [123.23], [], 2, 321]
result =[]
for i in range(len(l)):
    if type(i) == list:
        if len(i) != 0:
            result.append(i)
        else:
            result.append(i)
print(result)
