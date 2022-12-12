 Assignment Part-1

Q1. Why do we call Python as a general purpose and high-level programming language?

+ it is not specialized for any particular problem and used in variety of domains to program
+ easy to beginners. less code compare to other programming languages

Q2. Why is Python called a dynamically typed language?

+ no need to mention type of variable

Q3. List some pros and cons of Python programming language?

+ pros:  huge libraries, easy to pick, flexible to can pick any job role in it
+ cons: slow , high memory consumption

Q4. In what all domains can we use Python?

+ web development, gaming, big data

Q5. What are variable and how can we declare them?

+ just type the variable name and assign the value89
+ name = 'srinivas'

Q6. How can we take an input from the user in Python?

+ by using input function(method)
+ name = input('enter your name: ')

Q7. What is the default datatype of the value that has been taken as an input using input() function?

+ string

Q8. What is type casting?

+ converting data type from string to integer or vise-versa

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

+ no

 +yes, by using split() function to input value

Q10. What are keywords?

 +pre-defined words for specific use in compiler

Q11. Can we use keywords as a variable? Support your answer with reason.

+ no. it throws error

Q12. What is indentation? What's the use of indentaion in Python?

+ for represent block of code

Q13. How can we throw some output in Python?

+ through print() method

Q14. What are operators in Python?

+ arithmetic (+,-,%,*,/)
+ assignment,comparison,logical,bitwise,identify

Q15. What is difference between / and // operators?

+ / = divison operator , // = floor division operator

Q16. Write a code that gives following as an output.

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

user_num = int(input('enter a number')

if user_num%2 == 1 print('odd number')

elif user_num%2 == 0 print('even number')

Q18. What are boolean operator?

+ True or False

Q19. What will the output of the following?

```python

 1 or 0 = 1

 0 and 0 = 0

 True and False and True = False

 1 or 0 or 0 = 1

```

Q20. What are conditional statements in Python?

+ checks the specific logic to enter

Q21. What is use of 'if', 'elif' and 'else' keywords?

+ if ,elif conditions is correct the code continue inside thos blocks or the code executes in else block

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

```python
age = input('enter your age')
if(age >= 18) print('i can vote')
else print('I can't vote')
```


Q23. Write a code that displays the sum of all the even numbers from the given list.

```python

numbers = [12, 75, 150, 180, 145, 525, 50]
sum = 0
for( x in numbers)
  if(x%2 == 0)
   sum +=x

print(sum)
```

Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

```python
nums = input('please enter three numbers by maintaining space to give largest among three').split()
print(max(nums))
```

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop

```python

numbers = [12, 75, 150, 180, 145, 525, 50]

for(x in numbers)
  if( x != 500 and x !=150 and x%5 == 0 )
    print(x)
  elif(x == 150)
   continue
  elif(x== 500)
   break

```

Q26. What is a string? How can we declare string in Python?

+ a list of characters, var1 = 'srinu'

Q27. How can we access the string using its index?

```python-repl
var1 = 'srinivas'
print(var1[1])
```

Q28. Write a code to get the desired output of the following

```python
string = "Big Data iNeuron"
print(string[10:])
desired_output = "iNeuron"
```

Q29. Write a code to get the desired output of the following

```python
string = "Big Data iNeuron"
desired_output = "norueNi"
print( string[-1:-(len('iNeuron')+1):-1] )
```

Q30. Resverse the string given in the above question.

```python
print(string(::-1))
```

Q31. How can you delete entire string at once?

```python
string = ''
#or
del string #bad practices

```

Q32. What is escape sequence?

+ it is backslash(\\). used to output 'quotatation' and new line(\\n) in string

Q33. How can you print the below string?

```python-repl
pritn('iNeuron's Big Data Course')
```

Q34. What is a list in Python?

+ used to store multiple values in an order which are iterable also

Q35. How can you create a list in Python?

+ createsList = []

Q36. How can we access the elements in a list?

+ through index value

Q37. Write a code to access the word "iNeuron" from the given list.

```python-repl
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(lst[4][2])
```

Q38. Take a list as an input from the user and find the length of the list.

```python-repl
list = input('enter a list characters: ')
print(len(list))
```

Q39. Add the word "Big" in the 3rd index of the given list.

```python-repl
lst = ["Welcome", "to", "Data", "course"]
print(lst.insert(2, 'Big'))
```

Q40. What is a tuple? How is it different from list?

+ tuple similar to list but it is unchangable.

Q41. How can you create a tuple in Python?

+ createsTuple=()

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

+ createTuple = ('srinivas',)

Q43. Can two tuple be appended. If yes, write a code for it. If not, why?

```python-repl
createTuple = ('srinivas',)
createTuple + = ('peruri',)
print(createTuple)
```

Q44. Take a tuple as an input and print the count of elements in it.

```python-repl
createTuple = ('srinivas',)
createTuple += ('peruri',)
print( len(createTuple ))
```

Q45. What are sets in Python?

+ used to store list of items in unorder. sets are unchangable

Q46. How can you create a set?

```
thisset = {"apple", "banana", "cherry"}
print(type(thisset))
```

Q47. Create a set and add "iNeuron" in your set.

```python-repl
thisset = {"apple", "banana", "cherry"}
thisset.add(('iNeuron'))
print((thisset))
```

Q48. Try to add multiple values using add() function.


```
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
for x in tropical:
    thisset.add(x)
print(thisset)
```

Q49. How is update() different from add()?

+ add allows to add one item at time. update allow to add multiple values

Q50. What is clear() in sets?

+ remains to empty set

Q51. What is frozen set?

+ converts any data type to set which is unchangable like add ,remove

Q52. How is frozen set different from set?

+ set allow to modify like add or remove but frozenset throws error
