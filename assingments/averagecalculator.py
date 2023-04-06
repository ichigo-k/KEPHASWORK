#SCRIPT FOR AN AVERAGE CALCULATOR
values=[]
total =0
n= int(input("ENTER NUMBER OF VALUES"))
for numbers in range (n):
    num=int(input("ENTER A NUMBER"))
    values.append(num)
    total =total + values[numbers]
print(values)
print(total)
average=total/n
print(average)