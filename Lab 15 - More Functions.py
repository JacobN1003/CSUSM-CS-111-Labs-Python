#Functions
#Jacob Norenberg
#July 3, 2019

def treeTop():
    print("    ^")
    print("   /_\\")
    print("  /___\\")
    print(" /_____\\")
    print("/_______\\")

def treeTrunk():
    print("   | |")

def drawTrees(height, trees):
    while trees != 0:
        treeTop()
        for i in range(height):
            treeTrunk()
        trees -=1
flag = True
while flag:
    height = input("Enter tree height: ")
    trees = input("Enter how many trees: ")
    drawTrees(int(height), int(trees))
    more = input("Do you want more trees? <y/n> : ")
    if more!='Y' and more!='y':
        flag = False
