"""
BUBBLE SORT :
 
 Swapping of Adjacent elements until to get  ascending order of the given array.
 
 Time complexity: O(n2)
 Space complexity :O(n)
"""


arr=[2,8,6,3,7,1,4,5]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)
