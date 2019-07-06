#Sequential Search
#Jacob Norenberg
#July 3, 2019

def seqSearch(numbers,key):
   for i in range(10):
       if int(key) == numbers[i]:
           print(key + " was found at slot", i)
           return
   print("That number wasn't found.")

numbers = [12,-7,3,17,42,6,18,-15,0,1]
key = input("Search a number: ")
seqSearch(numbers, key)

