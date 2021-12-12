# Python-Practice-Problems

Python Practice problems repository is a collection of all problems that I have solved to build my foundation of the language and logical ability. The aim to make this repository is to collect all the fundamental commands and concepts learned in python such as list comprehension, Array, etc, and use them on basic problems such as adding lists, manipulating strings and making patterns, etc. 

### AIM:
Finding the right question for the coding practice can be time-consuming and one has to go through multiple platforms to find them. This collection is composed of problems from multiple platforms such as Hacker Rank, Leet code, Kaggle, etc. Tough questions have been divided into simple two or three-part problems for quick learning. Anyone with zero to intermediate experience in python is welcome to try these questions. 

### Problem Source:

1. Leet Code
2. Hacker Rank
3. Kaggle
4. W3 School

## Examples of the few of the problems from the collection:

#### 1. Remove repeating chacaters form following string x = "Python is the best programming language"
```
x = "Python is the best programming language"
x = x.lower()
y = list(x)
z = []
for i in y:
    if y.count(i) > 1:
        y.remove(i)
for i in y:
    if y.count(i) > 1:
        y.remove(i)
        
print(y)
```
![image](https://user-images.githubusercontent.com/64645859/145695710-e32cbb34-8877-490b-a2c1-0fed53384918.png)


#### 2. Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number
```
x= list(range(0,10))
print("Printing current and previous number sum in a range(10)")
for i in x:
    
    if i == 0:
        print("Current Number ",i, "Previous Number ",0, "Sum :  ", x[0])
    else:
        print("Current Number ",i, "Previous Number ",x[int(x.index(i))-1], "Sum :  ", i + int(x.index(i)-1))
  ```
  ![image](https://user-images.githubusercontent.com/64645859/145696002-39a97021-ac60-4cc6-81e7-6c3cdf4f208b.png)


#### 3. Finding the type of a character in a string - How many numbers, letters and punctuation are there in x = "Python3.7"
```
x = "Python3.7"

#Lets initialise first
Letters = []
numbers = []
punctuations = []

for i in x:
    if i.isalpha():
        Letters.append(i)
    elif i.isnumeric():
        numbers.append(i)
    else:
        punctuations.append(i)

print(Letters)
print(numbers)
print(punctuations)
```
![image](https://user-images.githubusercontent.com/64645859/145696049-13282879-6f13-4c9d-b67b-269f20c4aac3.png)


#### 4.General output with input command - Create a General Table for any interger.
```
digit = int(input("Please write a number"))
for i in range(1,11):
    print(digit,"*",i, "=" ,digit*i)
```
![image](https://user-images.githubusercontent.com/64645859/145696171-71fb3493-dd95-4b53-bcda-509dfa847726.png)

#### 5. Length, breadth, and height of a cuboid are 2,3,4 placed at origin. Make a list of all possible integer coordinate points first with list comprehension method and then loop method.
```
l=2
b=3
h=4

coodrinates = [[i,j,k] for i in list(range(0,l+1)) for j in list(range(0,b+1)) for k in list(range(0,h+1))]
print(coodrinates)

#OR By using loop:

coodrinates = []

for i in list(range(0,l+1)):
    for j in list(range(0,b+1)):
        for k in list(range(0,h+1)):
            coodrinates.append([i,j,k])
        
print(coodrinates)
```
![image](https://user-images.githubusercontent.com/64645859/145696145-7d1e9b6d-d43e-4b92-9278-540a8c6aa817.png)

