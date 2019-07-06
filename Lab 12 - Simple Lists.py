#Arrays / Lists
#Jacob Norenberg
#July 3, 2019

myArray = []
for i in range(1000):
    myArray.append(i*7.5)
num1 = input("Enter an integer 0-999: ")
if int(num1)>999 or int(num1)<0:
    print("Value out of range.")
else:
    print(myArray[int(num1)])
