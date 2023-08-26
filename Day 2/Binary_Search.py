def BinarySearch(arr,x,i,j):
    while i <= j :
        mid = i+(j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x :
            return BinarySearch(arr,x,mid+1,j)
        else :
            return BinarySearch(arr,x,i, mid-1)
    return -1

   
        


arr = [20,30,40,50,60,70,80,90]
x = 30
i = 0
j = len(arr)-1
result = BinarySearch(arr,x,i,j)
print(result)
