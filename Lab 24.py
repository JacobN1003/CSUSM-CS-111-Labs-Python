#Bubble Sort
#Jacob Norenberg
#July 3, 2019

n = int(input("Enter size of number list: "))
numList = []

for i in range(n):
    numbers = int(input("Enter number (" + str(i+1) + " of " + str(n) + "): "))
    numList.append(numbers)
print("Original list: ",numList)

for i in range(n):
    for j in range(n-1):
        if numList[j]>numList[j+1]:
            temp = numList[j]
            numList[j]=numList[j+1]
            numList[j+1]=temp
print("Sorted List: ",numList)
