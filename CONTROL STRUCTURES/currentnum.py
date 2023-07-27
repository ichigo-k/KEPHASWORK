number = int(input("Enter a number :\n"))
for num in range (number+1 ) :

    currentnumber = num
    
    print(f"Current number:{num}")
    if num == 0 :
        print("Previous number:0")
        num =1
    else:
        print(f"Previous number:{num-1}")

    sum =currentnumber + (num-1)
    print(f"Sum:{sum}")
    print(" ")
