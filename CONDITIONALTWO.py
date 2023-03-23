bill = 0
print("ESA pizza delivery")

size=input ("Which size do you want ? L,M,S")
peperoni=input("Do you want peperoni yes or no")
cheese=input ("Do you want cheese")
if size =="L" :
    bill +=100
elif size =="M" :
    bill +=85
else :
    size == "S" 
    bill +=50

if peperoni == "yes":
    bill += 10
if cheese == "yes":
    bill += 5

print(f"Your bill is {bill}")
    
