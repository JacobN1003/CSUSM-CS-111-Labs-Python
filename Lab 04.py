#If Statements
#Jacob Norenberg
#July 3, 2019

int1 = input("Enter an integer: ")
if int(int1)%2==0:
    if int(int1)%3==0 and int(int1)%5==0:
        print(int(int1), "is even and divisible by both 3 and 5.")
    else:
        print(int1 + " is even and not divisible by both 3 and 5.")
else:
    if int(int1)<0:
        print(int(int1), "is odd and negative.")
    else:
        print(int(int1), "is odd and positive.")
if int(int1)<=100 and int(int1)>=-100:
    print(int1 + " is in range.")
else:
    print(int1 + " is not in range.")