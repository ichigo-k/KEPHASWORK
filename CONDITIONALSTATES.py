age=input("Enter your age:")
if age <= "0":
    print("Age is invalid")
    if age >="18":
        print("You are of legal age")
elif age >= "80" :
    print("YOu are too old")
else :
    print ("you are tooyoung")


#BILL CALCULATOR
sze = input("Enter the size you want\n")

peperoni = input("Do you want extra peperonies")
print =("Enter yes or no")
cheese = input("Do you want extra chesee")
print =("Enter yes or no")

if sze=="L" and peperoni =="yes" and cheese=="yes" :
    print("your bill is 135")
    if sze =="L" and peperoni =="no" and cheese=="yes" :
        print("your bill is 125")
        if sze =="L" and peperoni =="yes" and cheese=="no" :
             print("your bill is 130")

if sze =="M" and peperoni =="yes" and cheese=="yes" :
    print("your bill is 100")
    if sze =="M" and peperoni =="no" and cheese=="yes" :
        print("your bill is 90")
        if sze =="M" and peperoni =="yes" and cheese=="no" :
             print("your bill is 95")

if sze =="S" and peperoni =="yes" and cheese=="yes" :
    print("your bill is 65")
    if sze =="S" and peperoni =="no" and cheese=="yes" :
        print("your bill is 55")
        if sze =="S" and peperoni =="yes" and cheese=="no" :
             print("your bill is 60")
else :
    print("Your selection is not available at the moment")

