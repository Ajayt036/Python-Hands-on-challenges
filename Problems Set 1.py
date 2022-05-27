#Q1. Remove repeating chacaters form following string |  x = "Python is the best programming language"

#Answer:
x  = "Python is the best programming language"
x = x.lower()
y = ""
for i in x:
    if i not in y:
        y=y + i
    else:
        pass
print(y)



#Q2. Reverse a string | "Ajay Thakur"
#Answer:
x = "Ajay Thakur"
print(x[::-1])




