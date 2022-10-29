"""
Merge sort

To split the array into two arrays continuously and sort the elements in two arrays.
And merge it into a single array.

Time complexity:
Space COmplexity:

"""



def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        merge_sort(L)
        merge_sort(R)
        arr.clear()
        while len(L)>0 and len(R)>0:
            if L[0]<=R[0]:
                arr.append(L[0])
                L.pop(0)
            else:
                arr.append(R[0])
                R.pop(0)
        for i in L:
            arr.append(i)
        for j in R:
            arr.append(j)
arr=[2,5,-1,7,4,3]
merge_sort(arr)
print(arr)
