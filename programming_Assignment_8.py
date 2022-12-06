### 1. Write a Python Program to Add Two Matrices?

mat1 = [[1,2,3],
        [6, -4, -9],
        [3,6,9]]

mat2 = [[6,9,3],
        [1,-1,1],
        [0, 9, 11]]
result = []
for i in range(len(mat1)):
    out = []
    for j in range(len(mat2)):
        out.append(mat1[i][j]+mat2[i][j])
    
    result.append(out)

print(result,'--sum of two matrix numbers-- ')

# 2. Write a Python Program to Multiply Two Matrices?
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            
            result[i][j] = A[i][k] * B[k][j]

print(result,'--multile--')

#3 Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]
'''
    00 - 00,10- 01,20-02
    01-10, 11=11, 21 =  12 
'''

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
    for j in range(len(result)):
        result [j][i] = X[i][j]
print(result,'--transpose--')


### 4. Write a Python Program to Sort Words in Alphabetic Order?

try:
    sentence = input('enter the words with separate spaces: ')
    words = [x for x in sentence.split()]
    words.sort()

    print('sorted order of words:')
    for word in words:
        print(word,end=' ')
except Exception as e:
    print(e)

print('\n')
# 5. Write a Python Program to Remove Punctuation From a String?

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("Enter the string: ")

outputString = ""

for char in string:
    if char not in punctuations:
        outputString += char
        
print(outputString)
