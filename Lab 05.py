#Switch Statement
#Jacob Norenberg
#July 3, 2019

numbers = {
    '0': "zero",
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine",
    '10': "ten"
}
int1 = input("Enter an integer 0-10: ")
if int(int1)<11 and int(int1)>=0:
    print("You have entered", numbers.get(int1, -1))
else:
    print(int1 + " is not in range.")