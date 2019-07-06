#Multiplication Table w/ Nested Loops
#Jacob Norenberg
#July 3, 2019

print("       1   2   3   4   5   6   7   8   9")
print("-----------------------------------------")
for x in range(9):
    x+=1
    print(x, "|   ", end="")
    for y in range(9):
        y+=1
        print(str(y*x).rjust(2), end="  ")
    print("\n")
