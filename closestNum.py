import numpy as np

# Python3 program to find the array element that is equal or closest to K.
# If there are two equal closest elements, it returns one of them. This
# program has a O(log(n)) run-time complexity.

def findClosest(arr, length, K): 
  
    #Edge cases, if the number is either too big or small, return closest element
    #either the biggest or smallest element in the array.
    if (K <= arr[0]): 
        print("Number of comparisons: 0")
        return arr[0] 
    if (K >= arr[length - 1]): 
        print("Number of comparisons: 0")
        return arr[length - 1] 
  
    #Binary search 
    i = 0; j = length; mid = 0; c = 0 #c stores number of comparisons
    while (i < j):  
        mid = int((i + j) / 2)
        c=c+1 #increment number of comparisons
        #print("mid is ",mid)
        if (arr[mid] == K): 
            print("Number of comparisons:",c)
            return arr[mid] 
  
        # If target is less than array  
        # element, then search in left 
        if (K < arr[mid]) : 
  
            # If target is greater than previous 
            # to mid, return closest of two 
            if (mid > 0 and K > arr[mid - 1]): 
                return getClosest(arr[mid - 1], arr[mid], K,c) 
  
            # Repeat for left half  
            j = mid 
          
        # If target is greater than mid 
        else : 
            if (mid < length - 1 and K < arr[mid + 1]): 
                return getClosest(arr[mid], arr[mid + 1], K,c) 
                  
            # update i 
            i = mid + 1
          
    # Only single element left after search 
    print("Number of comparisons:",c)
    return arr[mid] 
  
  
# Method to compare which one is the more close. 
# We find the closest by taking the difference 
# between the target and both values. It assumes 
# that val2 is greater than val1 and target lies 
# between these two. 
def getClosest(val1, val2, target,c): 
    count = c
    if (target - val1 >= val2 - target): 
        print("Number of comparisons:",count)
        return val2 
    else: 
        print("Number of comparisons:",count)
        return val1 
  
# Driver code 
#arr256 = np.zeros(256,dtype=int)
#arr512 = np.zeros(512,dtype=int)
#arr1024 = np.zeros(1024,dtype=int)
#arr2048 = np.zeros(2048,dtype=int)
#arr4096 = np.zeros(4096,dtype=int)
#arr8192 = np.zeros(8192,dtype=int)


#for i in range (256):
  #arr256[i] = int(i+np.floor(np.sqrt(i)))
  
#for i in range (512):   #fill array with values
  #arr512[i] = int(i+np.floor(np.sqrt(i)))
  
#for i in range (1024):  #fill array with values
  #arr1024[i] = int(i+np.floor(np.sqrt(i)))
  
#for i in range (2048):  #fill array with values
  #arr2048[i] = int(i+np.floor(np.sqrt(i)))
  
#for i in range (4096):  #fill array with values
  #arr4096[i] = int(i+np.floor(np.sqrt(i)))
  
#for i in range (8192):  #fill array with values
  #arr8192[i] = int(i+np.floor(np.sqrt(i)))
 

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
    
    print("--------------------\nArray size:",arrSizes[i])
    for k in range (10):
        keyGen(arrSizes[i],arrCurr)
        print("Key:",keys[i])
        print("Closest number:",findClosest(arrCurr, arrSizes[i], keys[i]), end ="\n\n") 


    
    


#print("--------------------\nArray size: 256")
#print("Key:",K)
#print("Closest number:",findClosest(arr256, 256, K), end ="\n\n") 

#print("--------------------\nArray size: 512")
#print("Key:",K)
#print("Closest number:",findClosest(arr512, 512, K), end ="\n\n") 

#print("--------------------\nArray size: 1024")
#print("Key:",K)
#print("Closest number:",findClosest(arr1024, 1024, K), end ="\n\n")

#print("--------------------\nArray size: 2048") 
#print("Key:",K)
#print("Closest number:",findClosest(arr2048, 2048, K), end ="\n\n") 

#print("--------------------\nArray size: 4096")
#print("Key:",K)
#print("Closest number:",findClosest(arr4096, 4096, K), end ="\n\n") 

#print("--------------------\nArray size: 8192")
#print("Key:",K)
#print("Closest number:",findClosest(arr8192, 8192, K), end ="\n\n") 
