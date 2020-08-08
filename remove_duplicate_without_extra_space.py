arr = list(map(int,input().split()))

# uses O(1) spaces

j = 0
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        arr[j] = arr[i]
        j += 1

arr[j] = arr[-1]

# assign slicing having no duplicates 
arr = arr[:j+1]  
print(arr)