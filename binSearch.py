import sys

def binarySearch(a, x):

    low = 0
    count = 0
    mid = 0
    high = 0
    
    high = len(a) - 1
    print("\nSearching for: ", x, "\n")
    
    while(low <= high):
        mid = (low + high) // 2
        if(a[mid] == x):
            print("\nFound:", a[mid], "at index position:", mid, "\n")
            sys.exit()
        elif(a[mid] < x):
            low = mid + 1
        else:
            high = mid -1

        print("Count: ", count, " | Low: ", low, " | Mid", mid, " | High: ", high)
        count = count + 1
        
    print("\nNot found in list\n")

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,22,23,27]
x = int(input("Enter number to search for: "))
binarySearch(a, x)
