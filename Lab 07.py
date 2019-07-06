#Do While Loop
#Jacob Norenberg
#July 3, 2019

even = 0
odd = 0
flag = True
while flag:
    a = input("Enter a positive integer (or -1 to quit): ")
    if int(a)>=0:
        if int(a)%2==0:
            even+=1
            print(a + " is even.")
        else:
            odd+=1
            print(a + " is odd.")
    elif int(a)==-1:
        flag = False
    else:
        print("Invalid Entry.")
print("Even Numbers:", even)
print("Odd Numbers:", odd)