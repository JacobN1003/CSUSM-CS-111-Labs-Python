#While Loops & Conditions
#Jacob Norenberg
#July 3, 2019

even = 0
odd = 0
flag = True
while flag:
    a = input("Enter a positive integer: ")
    if int(a)>=0:
        if int(a)%2==0:
            even+=1
            print(a + " is even.")
        else:
            odd+=1
            print(a + " is odd.")
    else:
        print("Invalid Entry.")
    b = input("Enter more? (y/n): ")
    if b!='Y' and b!='y':
        flag = False
print("Even Numbers:", even)
print("Odd Numbers:", odd)