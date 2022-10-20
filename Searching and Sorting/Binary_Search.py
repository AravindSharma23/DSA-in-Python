"""
BINARY SEARCH

Time complxity:O(logn)

How it works:
In Binary Search ,It divides an array in middle ,and binary search every time it divides
an array with middl
       


"""
l=list(map(int,input().split()))
num=int(input())
left = 0
right = len(l)-1
mid = 0
while (left<right):
    mid = (left+right)//2
    mid_num = l[mid]
    if mid_num == num:
        print("Index is ",mid)
        # count+=1 if count==1 ,print middle element index.
    if mid_num<num:
        left=left+1
    if mid_num>num:
        right=right-1
        



