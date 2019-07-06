#Variables
#Jacob Norenberg
#July 3, 2019

name = input("Enter your name: ")
major = input("Are you a CS major?: ")
mark = input("What is your favorite punctuation mark?: ")
int1 = input("Enter an integer: ")
int2 = input("Enter another integer: ")
div_result = float(int1) / float(int2)
rem_result = int(int1) % int(int2)
print("Hi " + name + ",", end=" ")
if major == "Yes" or major == "yes":
    print("You are a CS major ", end="")
else:
    print("You are not a CS major ", end="")
print("and your favorite punctuation is " + mark)
print(int1 + " divided by " + int2 + " is", div_result)
print(int1 + " divided by " + int2 + " is", int(div_result), "with a remainder of", rem_result)