"""
LINEAR SEARCH

Time complxity:O(n)

How it works:
       In linear search ,it continuously search for a particular element is present or not in an array.
       It Searches for n times(length).


"""
l=list(map(int,input().split()))
n=int(input())
for index,element in enumerate(l):
    if element == n:
        print("ENtering number and storing number is same")
        print("Index number is ",index)

