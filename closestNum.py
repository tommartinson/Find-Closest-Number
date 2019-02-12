import numpy as np

# Python3 program to find the array element that is equal or closest to K.
# If there are two equal closest elements, it returns one of them. This
# program has a O(log(n)) run-time complexity.

def findClosest(arr, length, K): 
  
    #Edge cases, if the number is either too big or small, return closest element,
    #either the biggest or smallest element in the array.
    if (K <= arr[0]): 
        print("Number of comparisons: 0")
        return arr[0] 
    if (K >= arr[length - 1]): 
        print("Number of comparisons: 0")
        return arr[length - 1] 
  
    #Binary Search 
    i = 0; j = length; mid = 0; c = 0 #c stores number of comparisons
    while (i < j):  
        mid = int((i + j) / 2)
        c=c+1 #increment number of comparisons
        
        if (arr[mid] == K): 
            print("# of comparisons:",c,end=' ')
            return arr[mid] 
  
        #If target is less than array  
        #element, search left side 
        if (K < arr[mid]) : 
  
            #If target is greater than previous 
            #to mid, return closest of two 
            if (mid > 0 and K > arr[mid - 1]): 
                return getClosest(arr[mid - 1], arr[mid], K,c) 
  
            #Repeat for left half  
            j = mid 
          
        #If target is greater than mid 
        else : 
            if (mid < length - 1 and K < arr[mid + 1]): 
                return getClosest(arr[mid], arr[mid + 1], K,c) 
                  
            # update i 
            i = mid + 1
          
    #Only one element left after search 
    print("# of comparisons:",c,end=' ')
    return arr[mid] 
  
  
#Method to compare which of the two is closest. 
#We find the closest by taking the difference 
#between the target and the values. It assumes 
#that val2 is greater than val1 and that the 
#target lies between those two. 
def getClosest(val1, val2, target,c): 
    count = c
    if (target - val1 >= val2 - target): 
        print("# of comparisons:",count,end=' ')
        return val2 
    else: 
        print("# of comparisons:",count,end=' ')
        return val1 
  

#Driver Code 
#Need to calculate for 10 different values of K. 
#Let K in each case be a random number between 0 and n+sqrt(n).
keys = np.zeros(10,dtype=int)   #array to hold 10 keys

def keyGen(length,arr):
    length=len(arr)
    for i in range (10):  #fill array with values
        keys[i]=np.random.randint(0, int(length+np.sqrt(length)), dtype=int)


        
arrSizes = [256, 512, 1024, 2048, 4096, 8192]  
for i in range(len(arrSizes)):
    arrCurr = np.zeros(arrSizes[i],dtype=int) #initialize to zeros
    for j in range (arrSizes[i]):
        arrCurr[j] = int(j+np.floor(np.sqrt(j)))
    print("-------------------------------------------------------\n")
    print("Array size:",arrSizes[i],"\n")
    for k in range (10):
        keyGen(arrSizes[i],arrCurr)
        print("Key:",keys[i],end=' ')
        ret = findClosest(arrCurr, arrSizes[i], keys[i])
        print("Closest number:",ret)
        #print("Closest number:",findClosest(arrCurr, arrSizes[i], keys[i]), "\n") 
    print("# of comparisons <=",int(np.log2(arrSizes[i])),"(C = log(",arrSizes[i],"))")

print("-------------------------------------------------------\n")
print("\nThe number of comparisons to find the closest number follows the equation:\nC=log(n) where C is the number of comparisons and n is the size of the array." )
print("\nTherefore, the run-time complexity of the algorithm is O(log(n)).")



