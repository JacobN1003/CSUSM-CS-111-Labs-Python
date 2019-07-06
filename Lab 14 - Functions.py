#Functions
#Jacob Norenberg
#July 3, 2019

#Write a function called treeTop that prints the top of a tree.  It should take no parameters and return void.
#Write a second function called treeTrunk that prints the trunk of a tree.  It should take one integer as a
#parameter for height (how many lines tall the trunk is), and also have a return type of void.  Finally, create
#a function called drawTrees that takes two integer parameters, one for height and one for the number of
#trees to draw.  drawTrees should use treeTop and treeTrunk.

#Have the user enter the height of the trees (same for all) and number of trees to draw.  Remember that to
#draw a backslash you need two backslashes.

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

height = input("Enter tree height: ")
trees = input("Enter how many trees: ")
drawTrees(int(height), int(trees))
