Python Practice problems repository is a collection of all problems that I have solved to build my foundation of the language and logical ability. The aim to make this repository is to collect all the fundamental commands and concepts learned in python such as list comprehension, Array, etc, and use them on basic problems such as adding lists, manipulating strings and making patterns, etc. 

## AIM
Finding the right question for the coding practice can be time-consuming and one has to go through multiple platforms to find them. This collection is composed of problems from multiple platforms such as Hacker Rank, Leet code, Kaggle, etc. Tough questions have been divided into simple two or three-part problems for quick learning. Anyone with zero to intermediate experience in python is welcome to try these questions.

I am updating this list of problems almost every day based on new interesting questions I find on the internet. You will see new problems getting added below in the collection every day. Examples of few such problems are given Below:

### Remove repeating chacaters form following string x = "Python is the best programming language"
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


