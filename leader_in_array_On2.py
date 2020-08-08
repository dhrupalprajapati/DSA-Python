# Using O(n**2) time complexity
# leader means element having it's all right side occurances ar less or equal then that element.
# last element is also a leader because no element occur behind that, i.e. the last one.

arr = list(map(int,input().rstrip().split()))
total_elements = len(arr)

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j] >= arr[i]:
            break
    if j+1 == total_elements: # found mistake over this condition
        print(arr[i]) 
