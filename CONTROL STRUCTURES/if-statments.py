# #LOGICAL OPERATORS
# #RELATIONAL OPERATORS
# a= 12
# b=9
# print(a>=b and a!=b)

# level=int(input("Enter a level:\n"))
# gpa=float(input("Enter your gpa:\n"))
# print(level >= 300 and gpa >=2)

# fnum=int(input("Enter first number:"))
# snum=int(input("Enter second number:"))


# if fnum > snum :
#     print(F"{fnum } is the largest")
# else :
#     print(f"{snum} is the largest value")

print("1.Transfer Moneny\n2.Momo Pay and Pay Bills \n3.Airtime and Bundles")
user_input=int(input("Select an option\n"))

if user_input==1:
    print("""
        1.Momo User
        2.Non-momo user
        3.Send with care

    """)
    user_input=int(input())
    #NESTED IF STATEMENT
    if user_input==1:
        print("Momo Number")
        if user_input==1:
            print("Momo Number")
    elif user_input==2:
        print("Non momo user")
    elif user_input==3:
        print("Momo Number")
    else:
        print("invalid option")

elif user_input==2:
    print("Momo Pay ......")
elif user_input==3:
    print("Airtime ....")
else:
    print("Invalid Input please try again")
