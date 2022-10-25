"""
INSERTION SORT:
       Time complexity: O(n2)
       Space Complexity:O(1)
       
       Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
       The array is virtually split into a sorted and an unsorted part. 
       Values from the unsorted part are picked and placed at the correct position in the sorted part.
"""



arr=[int(x) for x in input().split()]
for i in range(1,len(arr)):
    current_val=arr[i]
    position = i
    while(position >0 and (arr[position-1]>current_val)):
        arr[position]=arr[position-1]
        position=position-1
        
    if position != i :
        arr[position]= current_val
        
print(arr)
