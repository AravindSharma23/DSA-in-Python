"""
SELECTION SORT:
It's an improved version of bubble sort.
It places small numbers in beginning or places large numbers in the end of the list.


TIME COMPLEXITY :O(n2)
SPACE COMPLEXITY : O(1)

"""

arr=[23,9,34,-1,4,80,27,0,3,2]
for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index] = arr[min_index],arr[i]
print(arr)
