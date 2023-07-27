import trywork as values

print("""
    1.Addition
    2.Multiplication
    3.Division
    4.Subtraction
""")

option =input("What operation should be performed?\n")

if option == "1" :
   total = values.add
   print(total)
elif option == "2":
   total = values.mul
   print(total)
elif option == "3":
   total = values.div
   print(total)
elif option == "4":
   total = values.sub
   print(total)
else:
   print("Wrong option")




