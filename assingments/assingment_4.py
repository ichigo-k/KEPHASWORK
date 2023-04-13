#SCRIPT FOR AN AVERAGE CALCULATOR
values=[]
total =0
n= int(input("ENTER TOTAL NUMBER OF VALUES\n"))
for numbers in range (n):
    num=int(input("ENTER A NUMBER\n"))
    values.append(num)
    total =total + values[numbers]
print(total)
average=total/n
print(average)